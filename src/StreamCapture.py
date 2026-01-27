import cv2
import urllib.request
import numpy as np

url = "http://192.168.1.131:80/capture"

while True:
    img_resp = urllib.request.urlopen(url, timeout=3)
    img_np = np.frombuffer(img_resp.read(), dtype=np.uint8)
    frame = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    if frame is None:
        continue

    cv2.imshow("ESP32-CAM", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
