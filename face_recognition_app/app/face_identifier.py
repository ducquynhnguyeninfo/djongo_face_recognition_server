import face_recognition
import cv2

import ntpath
import os


# Goi va truy cao webcam #0, webcam mac dinh
video_capture = cv2.VideoCapture(0)

# Doc trong thu muc cac hinh anh co san da duoc dinh danh
labeled_image_paths = []
for root, dirs, files in os.walk('../../../../face_regconition/images/labeled_images/'):
    for file in sorted(files):
        labeled_image_paths.append(os.path.join(root, file))

# Doc du lieu hinh anh da duoc dinh danh san
known_face_encodings = []
known_face_names = []
for path in labeled_image_paths:
    head, tail = ntpath.split(path)
    file_name = tail or ntpath.basename(head)

    image = face_recognition.load_image_file(path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(file_name.split(r'.')[0])

# Initialize some variables
face_frame_positions = []
face_frame_encodings = []
face_names = []
process_this_frame = True

while True:
    # Lay ra 1 frame tu video
    ret, frame = video_capture.read()

    # Thay doi kich thuoc cua video de xu ly nhanh hon
    ensmall_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Chuyen buc hinh tu chuan color BGR (openCV) sang chuan color RGB (face_recognition_app)
    rgb_small_frame = ensmall_frame[:, :, ::-1]

    # Chi xu ly 1 buc hinh de tiet kiem hieu nang
    if process_this_frame:
        # Tim tat ca cac khuon mat xuat hien trong buc hinh hien tai
        face_frame_positions = face_recognition.face_locations(rgb_small_frame, model='cnn')
        # Model = cnn chinh xac hon nhung toc do fps cham hon
        face_frame_encodings = face_recognition.face_encodings(rgb_small_frame, face_frame_positions)

        face_names = []
        for face_encoding in face_frame_encodings:
            # kiem tra neu khuon mat khop voi khuon mat da duoc dinh danh
            # Nguong chap nhan la 55%
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.55)
            name = "Unknown"
            # Neu co khuon mat khop voi khuon mat da dinh danh truoc
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # hien thi ket qua
    for (top, right, bottom, left), name in zip(face_frame_positions, face_names):
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
    cv2.imshow('Face Recognition', frame)

    # An nut 'q' tren ban phim de thoat chuong trinh
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giai phong bien va bo nho
video_capture.release()
cv2.destroyAllWindows()
