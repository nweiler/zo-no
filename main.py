# https://towardsdatascience.com/implementing-real-time-object-detection-system-using-pytorch-and-opencv-70bac41148f7
# https://pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/
# https://www.mygreatlearning.com/blog/object-detection-using-tensorflow/


import socket
import cv2
import torch
stream = cv2.VideoCapture(0) # 0 means read from local camera.
window_name = "FPS Single Loop"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

img, frame = stream.read()
#img = img[:, ::-1]
cv2.imshow(window_name, frame)
cv2.waitKey(0)
stream.release()
cv2.destroyAllWindows()


#server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#import cv2
#camera_ip = "rtsp://username:password@IP/port"
#stream = cv2.VideoCapture(camera_ip)

#from torch import hub # Hub contains other models like FasterRCNN
#model = torch.hub.load( \
                      #'ultralytics/yolov5', \
                      #'yolov5s', \
                      #pretrained=True)

