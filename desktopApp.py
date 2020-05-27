import numpy as np
import pickle
import cv2
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer



default_image_size = tuple((256, 256))

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


fileobject = open('cnn_model.pkl', 'rb')
model = pickle.load(fileobject)
imgpath='potato__healthy.jpeg'

imar = convert_image_to_array(imgpath)
npimagelist = np.array([imar], dtype=np.float16) / 225.0

PREDICTEDCLASSES2 = model.predict(npimagelist)
print(PREDICTEDCLASSES2)


label_classes = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']

# max_value = max(my_list)
# max_index = my_list.index(max_value)

#max_value = max(PREDICTEDCLASSES2[0])
max_index = np.argmax(PREDICTEDCLASSES2, axis=1)

print(label_classes[max_index[0]])
#Potato___Early_blight

#label_list = []
#label_binarizer = LabelBinarizer()
#image_labels = label_binarizer.fit_transform(label_list)
#pickle.dump(label_binarizer,open('label_transform.pkl', 'wb'))
#n_classes = len(label_binarizer.classes_)

#print(label_binarizer.classes_)

#label_binarizer_object = open('label_transform.pkl', 'rb')
#label_binarizer = pickle.load(label_binarizer_object)

#print (label_binarizer.classes_[PREDICTEDCLASSES2])