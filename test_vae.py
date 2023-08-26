import argparse
ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())
ap.add_argument('pos', type=str,help='path to input image (either good_img or defect_img)')
args = vars(ap.parse_args())

# import the libraries
import pickle
import numpy as np
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import cv2

print("[INFO] loading autoencoder...")
autoencoder = load_model('autoencoder.model')

	
# compute the q-th quantile of the errors which serves as our
# threshold to identify anomalies -- any data point that our model
# reconstructed with > threshold error will be marked as an outlier
thresh = 0.04256027564406395
print("[INFO] testing model...")
img_test = cv2.imread("/code/"+args['pos'])
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY).reshape((1,64,64,1))
recon_test = autoencoder.predict(img_test)
mse_test = (img_test - recon_test)**2

idxs = np.where(np.array(mse_test) >= thresh)[0]
if (len(idxs)>0):
	print(f"***\nResult: DEFECTIVE")
else:
	print(f"***\nResult: GOOD")

