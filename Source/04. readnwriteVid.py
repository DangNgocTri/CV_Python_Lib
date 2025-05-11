import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

def VideoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def VideoFromFile():
    root = os.getcwd()
    VidPath = os.path.join(root, 'Photos\TestVid.mp4')
    cap = cv.VideoCapture(VidPath)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv.imshow('Input Video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break

def writeVideoToFile():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')                 # fourcc là mã codec dùng để nén video.
    root = os.getcwd()
    outPath = os.path.join(root, 'Photos\\Webcam.avi')      #outPath: tạo đường dẫn đến file video sẽ được lưu

    out = cv.VideoWriter(outPath, fourcc, 20.0, (640,480))  
        # Tạo một đối tượng VideoWriter để ghi các frame vào file video.
        # 20.0: số khung hình trên giây (fps).
        # (640,480): độ phân giải của khung hình.

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow('Webcam', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()
        # cap.release(): giải phóng camera.
        # out.release(): đóng file video.
        # cv.destroyAllWindows(): đóng tất cả cửa sổ hiển thị của OpenCV.

if __name__ == '__main__':
    # VideoFromWebcam()
    # VideoFromFile()
    writeVideoToFile()