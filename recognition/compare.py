from encode import fetch,face_recognition

#Fetching the names and encodings from the database using custom-defined fucntions
# names,encodings = fetch()

# print(names,encodings)

def compare_faces(known_names,known_encodings,unknown_img):
    unknown_face = face_recognition.load_image_file(unknown_img)
    unknown_encoding = face_recognition.face_encodings(unknown_face)

    # results = face_recognition.compare_faces(known_face_encodings=known_encodings[1],face_encoding_to_check=unknown_encoding,tolerance=0.6)
    counter = 0
    for encoding in known_encodings:
        result = face_recognition.compare_faces(known_face_encodings=encoding,face_encoding_to_check=unknown_encoding,tolerance=0.6)
        counter += 1
        if(result[0]) :
            break
    
    return known_names[counter-1]
