import cv2
import redis
import numpy as np
 
client = redis.Redis()
client_channel = client.pubsub()

client_channel.subscribe("meet-1")

for item in client_channel.listen():    
    if item["type"] != "message":
        continue
    frame = np.frombuffer(item["data"], dtype="uint8").reshape(480, 640, 3)
    cv2.imshow("Video stream", frame)
    if cv2.waitKey(1) & 0xFF == ord("f"):
        break
 
client_channel.unsubscribe()
cv2.destroyAllWindows()