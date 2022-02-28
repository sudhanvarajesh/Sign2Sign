import cv2, pickle
import numpy as np
import tensorflow as tf
from cnn_tf import cnn_model_fn
import os
import sqlite3
from glob import glob
from sklearn.utils import shuffle
from PIL import Image
from keras.models import load_model

def pickle_images_labels():
	images_labels = []
	images = glob("words/1/*.jpg")
	images.sort()
	for image in images:
		print(image)
		label = image[image.find(os.sep)+1: image.rfind(os.sep)]
		img = cv2.imread(image, 0)
		images_labels.append((np.array(img, dtype=np.uint8), int(label)))
	return images_labels


image_x, image_y = 50, 50
with open("test_images", "rb") as f:
	test_images = np.array(pickle.load(f))
test_images = np.reshape(test_images, (test_images.shape[0], image_x, image_y, 1))


model = load_model('cnn_model_keras2.h5')
pred_probabs = model.predict(test_images)
