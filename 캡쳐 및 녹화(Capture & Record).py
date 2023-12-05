import datetime
import cv2

capture = cv2.VideoCapture("./image/oppen.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("./image/oppen.mp4")


    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H_%M_%S")

    key = cv2.waitKey(33)

    # 27 = ESC, 26 = Ctrl + Z, 24 = Ctrl + X, 3 = Ctrl + C
    if key == 27:
        break

    elif key == 26:
        print("캡쳐")
        cv2.imwrite("./image" + str(now) + ".png", frame)
    elif key == 24:
        print("녹화시작")
        record = True
        video = cv2.VideoWriter("./image" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    elif key == 22:
        print("녹화 중지")
        record = False


    if record == True:
        print("녹화중..")
        video.write(frame)



capture.release()
cv2.destroyAllWindows()