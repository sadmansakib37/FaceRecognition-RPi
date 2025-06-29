
from picamera import PiCamera
from time import sleep
import os

cam = PiCamera()
os.makedirs('dataset', exist_ok=True)

for i in range(50):
    cam.resolution = (512, 512)
    print(f"Capturing image {i+1}")
    cam.start_preview()
    sleep(2)
    cam.capture(f'dataset/{i}.jpg')
    cam.stop_preview()
