import cv2
from lib.pyzbarMaster.pyzbar.pyzbar import decode
import numpy as np


IS_VALID = False
LAST_QRCODE = ""


def get_coordinates(qrcode, frame):
    '''Extraire les coordonnées du QR code et l'encadre'''
    rect_points = qrcode.polygon
    if len(rect_points) == 4:
        pts = cv2.polylines(frame, [np.array(rect_points, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
        

def decode_qrcode(qrcode):
    '''Décode le QR code'''
    qr_data = qrcode.data.decode('utf-8')
    qr_type = qrcode.type
    return qr_data, qr_type


def print_qrcode(qrcode, qr_data, qr_type, frame):
    '''Afficher le texte du QR code sur l'image'''
    cv2.putText(frame, f'{qr_data} ({qr_type})', (qrcode.rect[0], qrcode.rect[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
   

def get_last_qrcode():
    '''Donne le dernier qrcode détecté'''
    #TODO  
    return


def set_last_qrcode(qrcode, qr_data, qr_type):
    '''Remplace le dernier qrcode détecté'''
    #TODO  
    return


def save_qrcode(qrcode, qr_data, qr_type):
    '''Sauvegarde le qrcode détecté'''
    #TODO
    return


def validate_the_qrcode(qr_data):
    '''Valide la détection du qrcode'''
    if (LAST_QRCODE == qr_data):
        IS_VALID = True
    return IS_VALID


def detect_qrcodes(frame):
    '''Détecte les qrcodes de la vidéo'''
    qrcodes = decode(frame)
    for qrcode in qrcodes:
        get_coordinates(qrcode, frame)
        qr_data, qr_type = decode_qrcode(qrcode)
        print_qrcode(qrcode, qr_data, qr_type, frame)
    return frame


def detect_and_save_qrcodes(frame):
    '''Détecte les qrcodes de la vidéo et les sauvegarde dans un document'''
    qrcodes = decode(frame)
    for qrcode in qrcodes:
        get_coordinates(qrcode, frame)
        qr_data, qr_type = decode_qrcode(qrcode)
        if qr_data != get_last_qrcode():
            save_qrcode(qrcode, qr_data, qr_type)
            set_last_qrcode(qrcode, qr_data, qr_type)
        print_qrcode(qrcode, qr_data, qr_type, frame)
    return frame


def detect_and_check_qrcodes(frame):
    '''Détecte les qrcodes de la vidéo et vérifie qui correspond à un qrcode enregistré'''
    qrcodes = decode(frame)
    for qrcode in qrcodes:
        get_coordinates(qrcode, frame)
        qr_data, qr_type = decode_qrcode(qrcode)
        validate_the_qrcode(qr_data)        
        print_qrcode(qrcode, qr_data, qr_type, frame)
    return frame