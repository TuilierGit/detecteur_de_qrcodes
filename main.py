import cv2
from qrcodes import detect_qrcodes
from camera import start_camera, show_camera, free_camera


if __name__ == '__main__':
    cap = start_camera()

    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la caméra")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur lors de la lecture de la caméra")
            break

        # Détecter et afficher les QR codes dans l'image
        frame_with_qr = detect_qrcodes(frame)
        show_camera(frame_with_qr)

        # Si on appuie sur 'q', quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    free_camera(cap)