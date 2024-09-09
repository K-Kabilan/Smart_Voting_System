import cv2, sys, numpy, os ,sqlite3
haar_file = r'C:\Users\kabil\OneDrive\Desktop\server\Blockchain\e_voting_blockchain\Person Identification\haarcascade_frontalface_alt2.xml'
datasets = r'C:\Users\kabil\OneDrive\Desktop\server\Blockchain\e_voting_blockchain\Person Identification\datasets'

def detect(name):
    sub_data =name
    path = os.path.join(datasets, sub_data) 
    if not os.path.isdir(path): 
        os.mkdir(path)  
    (width, height) = (130, 100)     

    face_cascade = cv2.CascadeClassifier(haar_file) 
    webcam = cv2.VideoCapture(0)  
    
    count = 1
    while count<50:  
        (_, im) = webcam.read() 
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
        for (x, y, w, h) in faces: 
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
            count += 1
            face = gray[y:y + h, x:x + w] 
            face_resize = cv2.resize(face, (width, height)) 
            cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
        
        cv2.imshow('OpenCV', im) 
    
        key = cv2.waitKey(10)
        if key == ord("q"): 
            break
            
    webcam.release()
    cv2.destroyAllWindows()