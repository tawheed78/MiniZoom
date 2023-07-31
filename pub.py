import cv2

import redis

video = cv2.VideoCapture(0)
height = int(video.get(4) / 2)
width = int(video.get(3) / 2)

server = redis.Redis()

while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imshow('Admin Cam', frame)
        server.publish("meet-1", frame.tobytes())
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print('No frames')
        break
video.release()