import cv2

# Load trained model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('Model/Training_data.yml')

# Variable Init Section
x, y, w, h = 0, 0, 0, 0
tempLabel = ''


# Detect and face Frame drawing function
def face_detector(img):
    global x, y, w, h, roi
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting colored image to grayscale

    # Load prebuilt classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Obtain face coordinates
    faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=7)

    if faces == ():
        return img, []

    # Draw the frame arround face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (500, 500))

    return img, roi


# Dict to better show which face is detecting
name = {0: 'Nihilus', 1: 'Malak', 2: 'Kryat'}

# Video Capture
cap = cv2.VideoCapture(1)

while True:
    ret, img_frame = cap.read()  # Read frames from camera

    image, req_face = face_detector(img_frame)  # Call the face detector function

    try:
        req_face = cv2.cvtColor(req_face, cv2.COLOR_BGR2GRAY)
        label, confidence = face_recognizer.predict(req_face)  # Predict name
        print('Confidence :', confidence) #Level of confidence
        print('Label :', label) #Face label

        tempLabel = label

        face_label = name[label]  # Name to show in frame

        
        if (label == tempLabel) and (confidence < 50):
            cv2.putText(image, face_label, (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0),2)  # when confidence is high show the name aligned with frame
        else:
            cv2.putText(image, 'Unknown', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255),2)  # when a face is on camera but is not recognized show unknown 
        cv2.imshow('Face Recognizer', image)

    except:
        cv2.putText(image, '', (50, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255),2) #When there is no face no need to show anything
        cv2.imshow('Face Recognizer', image)

    if cv2.waitKey(1) == 13:  # exit if user presses enter
        break

cap.release()  # release camera usage
cv2.destroyAllWindows()
