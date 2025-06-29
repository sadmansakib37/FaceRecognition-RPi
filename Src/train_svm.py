import os
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
from sklearn import svm
import pickle

# Load dataset
image_dir = 'dataset'
images = []
labels = []

for idx, filename in enumerate(os.listdir(image_dir)):
    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(image_dir, filename)).convert('L').resize((224, 224))
        img_np = np.array(img).flatten() / 255.0
        images.append(img_np)
        labels.append(1 if 'Imran' in filename else 2)  # Dummy logic, adjust as needed

X = np.array(images)
y = np.array(labels)

# PCA
pca = PCA(n_components=100)
X_pca = pca.fit_transform(X)

# SVM Training
clf = svm.SVC()
clf.fit(X_pca, y)

# Save models
with open('../models/svm_model.sav', 'wb') as f:
    pickle.dump(clf, f)
with open('../models/pca_uns.sav', 'wb') as f:
    pickle.dump(pca, f)