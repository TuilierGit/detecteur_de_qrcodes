import cv2

def start_camera():
    '''Démarre la caméra via la lib cv2 et retourne la variable'''
    cap = cv2.VideoCapture(0)
    return cap


def show_camera(frame_with_qr):
    '''Afficher l'image avec les QR codes détectés'''
    cv2.imshow("QR Code Detector", frame_with_qr)


def free_camera(cap):
    '''Libérer la caméra et fermer les fenêtres''' 
    cap.release()
    cv2.destroyAllWindows()
