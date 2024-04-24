import mediapipe as mp
import cv2 


#Inicializa  o opencv e o mediapipe
webcam = cv2.VideoCapture(0)
face_detector = mp.solutions.face_detection

face_recognizer = face_detector.FaceDetection()
draw = mp.solutions.drawing_utils

#def extract_facial_features(image):
    
#    return

while True: 
    
    #Ler informações da webcam
    verifier, frame = webcam.read()
    
    if not verifier: 
        break
    #reconhecer os rostos
    list_faces = face_recognizer.process(frame)
    
    if list_faces.detections:
        for face in list_faces.detections : 
                #desenhar os rostos na imagem
            draw.draw_detection(frame, face)
    cv2.imshow("Tela", frame)
    

    #quando aperta esc sai
    if cv2.waitKey(5) == 27: 
        break
    
webcam.release()