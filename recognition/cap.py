import cv2
from compare import compare_faces
from encode import fetch

names,encodings = fetch()

face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

counter = 0

while True:
    ret,video_data = video_cap.read()
    counter += 1

    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,h,w) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
        img = cv2.imread(video_data)
        print(compare_faces(names,encodings,img))
        
    
    # if counter % 30 == 0:
    #     if(faces):
    #         result = compare_faces(known_names=names,known_encodings=encodings,unknown_img=video_data)
    #         print(faces)
    

    cv2.imshow('Cam',video_data)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()