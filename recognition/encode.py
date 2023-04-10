import face_recognition
import numpy as np
import os
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['Users']
collection = db['Encodings']

known_faces = 'C:\\Users\\Simon Riley\\Desktop\\face-recognition\\images'

#Looping through all the registered faces
def push():
    for image in os.listdir(known_faces):

        if image.endswith('.jpg'):    
            face = face_recognition.load_image_file(os.path.join(known_faces,image))
            encoding = face_recognition.face_encodings(face)[0]
            enc = encoding.tolist()
            name = str(image)
            doc = {
                'name':name[:-4],
                'encoding':encoding.tolist()
            }
            collection.insert_one(doc)

def fetch():
    known_faces_names = []
    known_face_encodings = []


    encodings = collection.find()
    for doc in encodings :
        known_face_encodings.append(np.array(doc['encoding']))
        known_faces_names.append(doc['name'])

    return known_faces_names,known_face_encodings
