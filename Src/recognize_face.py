import picamera
from time import sleep
from PIL import Image
import numpy as np
import pickle

# Load trained models
model_path = '../models/svm_model.sav'
pca_path = '../models/pca_uns.sav'
model = pickle.load(open(model_path, 'rb'))
pca = pickle.load(open(pca_path, 'rb'))

# Initialize camera
camera = picamera.PiCamera()
frames = int(input("Enter number of frames to process: "))

v1 = v2 = v3 = 0

for fr in range(frames):
    camera.resolution = (512, 512)
    camera.start_preview()
    sleep(2)
    camera.capture('cur_frame.jpg')
    camera.stop_preview()

    img = Image.open('cur_frame.jpg').convert('L').resize((224, 224))
    img_np = np.array(img).flatten() / 255.0
    img_pca = pca.transform([img_np])
    pred = model.predict(img_pca)[0]

    v1, v2 = v2, v3
    v3 = pred

    if v1 == 1 or v2 == 1 or v3 == 1:
        print("Imran (Class 1) seen on camera")
    elif v1 == 2 or v2 == 2 or v3 == 2:
        print("Sadman (Class 2) seen on camera")
    else:
        print("Background or Unknown face!")
