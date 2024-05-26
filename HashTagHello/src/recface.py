import cv2
import mediapipe as mp

# Inicializar o OpenCV
webcam = cv2.VideoCapture(0)

# Inicializar o MediaPipe
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while webcam.isOpened():
    # Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break
    
    # Recpnhecer os rostos que tem na imagem
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhar os rostos na imagem
            desenho.draw_detection(imagem, rosto)
    cv2.imshow('Rostos na webcam', imagem)
    
    # Quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()