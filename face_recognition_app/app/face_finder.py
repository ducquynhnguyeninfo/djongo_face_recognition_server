import face_recognition
import cv2

import ntpath
import os

import path as path

from djongo_face_recognition_server import settings
# from .models import Face


class FaceIdentifier:
    known_face_encodings = []
    known_face_names = []
    process_this_frame = True
    face_frame_positions = []
    face_frame_encodings = []
    face_names = []

    def __init__(self):
        self.loadKnownFaces()

    def loadKnownFaces(self):
        # read from database ??

        # Doc trong thu muc cac hinh anh co san da duoc dinh danh
        print('start loading known faces...')
        labeled_image_paths = []
        folder = settings.STATIC_ROOT + '/labeled_images/'
        for root, dirs, files in os.walk(folder):
            print('examining {0}...'.format(len(files)))
            for file in sorted(files):
                labeled_image_paths.append(os.path.join(root, file))
        for path in labeled_image_paths:
            head, tail = ntpath.split(path)
            file_name = tail or ntpath.basename(head)

            image = face_recognition.load_image_file(path)
            face_encoding = face_recognition.face_encodings(image)[0]
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(file_name.split(r'.')[0])
        print('done loading {0} known faces...'.format(len(self.known_face_names)))

    def handleFace(self, face):
        resized_frame = cv2.resize(face, (0, 0), fx=0.25, fy=0.25)
        # Chuyen buc hinh tu chuan color BGR (openCV) sang chuan color RGB (face_recognition_app)
        rgb_small_frame = resized_frame[:, :, ::-1]

        self.face_frame_encodings = face_recognition.face_encodings(rgb_small_frame)

    def handleFrame(self, frame):
        resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Chuyen buc hinh tu chuan color BGR (openCV) sang chuan color RGB (face_recognition_app)
        rgb_small_frame = resized_frame[:, :, ::-1]

        self.face_names = []
        for face_encoding in self.face_frame_encodings:
            # kiem tra neu khuon mat khop voi khuon mat da duoc dinh danh
            # Nguong chap nhan la 55%
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.55)
            name = "Unknown"
            # Neu co khuon mat khop voi khuon mat da dinh danh truoc
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            self.face_names.append(name)

        if self.process_this_frame:
            # Tim tat ca cac khuon mat xuat hien trong buc hinh hien tai
            self.face_frame_positions = face_recognition.face_locations(rgb_small_frame, model='cnn')
            # Model = cnn chinh xac hon nhung toc do fps cham hon
            self.face_frame_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_frame_positions)

            self.face_names = []
            for face_encoding in self.face_frame_encodings:
                # kiem tra neu khuon mat khop voi khuon mat da duoc dinh danh
                # Nguong chap nhan la 55%
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.55)
                name = "Unknown"
                # Neu co khuon mat khop voi khuon mat da dinh danh truoc
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # hien thi ket qua
        for (top, right, bottom, left), name in zip(self.face_frame_positions, self.face_names):
            # phong to vi tri cua khuon mat len 4 lan, vi ta da thu nho hinh anh 4 lan de xu ly
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Ve mot hinh vuong tai vi tri khuon mat
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), thickness=2)

            # Ve ten cua nguoi da duoc dinh danh
            cv2.rectangle(frame, (left, bottom - 40), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Hien thi ket qua
        return frame
        # cv2.imshow('Face Recognition', frame)

    def stop(self):
        cv2.destroyAllWindows()
