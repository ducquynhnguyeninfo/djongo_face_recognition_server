import json

import cv2
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from rest_framework.generics import ListAPIView

from face_recognition_app.app.face_finder import FaceIdentifier


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def stream():
    cap = cv2.VideoCapture(0)
    face_identifier = FaceIdentifier()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break
        result = face_identifier.handleFrame(frame)

        cv2.imwrite('demo.jpg', result)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')


def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')


def ws_channel(request):
    if request.method == "POST":
        face_data = request.POST.get("data")
        # char_choice = request.POST.get("character_choice")
        return redirect(
            '/play/%s?&choice=%s'
            %(room_code, char_choice)
        )
    return render(request, "index.html", {})


class ImageViewSet(ListAPIView):
    # queryset = UploadImageTest.objects.all()
    # serializer_class = ImageSerializer
    def post(self, request, *args, **kwargs):
        image = request.data['image']
        # image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
