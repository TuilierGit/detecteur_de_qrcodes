import cv2
from lib.pyzbarMaster.pyzbar.pyzbar import decode
import numpy as np

def detect_qrcodes(frame):
    '''Détecte les qrcodes de la vidéo'''
    qrcodes = decode(frame)
    for qrcode in qrcodes:
        # Extraire les coordonnées du QR code
        rect_points = qrcode.polygon
        if len(rect_points) == 4:
            pts = cv2.polylines(frame, [np.array(rect_points, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Décoder le QR code
        qr_data = qrcode.data.decode('utf-8')
        qr_type = qrcode.type
        
        # Afficher le texte du QR code sur l'image
        cv2.putText(frame, f'{qr_data} ({qr_type})', (qrcode.rect[0], qrcode.rect[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame
