import datetime

from PIL import ImageGrab   # 'pil' for Pillow and imageGrab for grab the image
import numpy as np      #Numpy numeric python
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f'{time_stamp}.mp4'
force = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, force, 20.0, (width, height))

webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_clr = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()

    frame_height, frame_width, _ = frame.shape
    img_clr[0:frame_height, 0: frame_width, :100] = frame[0: frame_height, 0:frame_width, :100]
    cv2.imshow('Secret Capture', img_clr)

    # cv2.imshow('webcam', frame)
    capture_video.write(img_clr)
    if cv2.waitKey(1) == ord('q'):
        break
