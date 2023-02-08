import PySimpleGUI as sg
import cv2
import numpy as np
import os
from imutils import paths
import face_recognition
#import argparse
import pickle

def foto(nama, frame):
    if not os.path.exists(f'dataset/{nama}'):
        os.makedirs(f'dataset/{nama}')
    # buat perulangan untuk mengambil 35 gambar
    for i in range(35):
        # simpan gambar ke dalam folder dataset
        cv2.imwrite(f'dataset/{nama}/{nama}_{i}.jpg', frame)
        # tambahkan delay 100ms
        cv2.waitKey(100)

imagePaths = list(paths.list_images("dataset"))
knownEncodings = []
knownNames = []
def train():
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]

        # load the input image and convert it from RGB (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,model="hog")

        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)

        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sg.theme("BluePurple")
    layout = [
        [sg.Text("R E G I S T R A S I", font='Any 25', text_color='#5990F6')],
        [sg.Image(filename="", key="-IMAGE-")],
        [
            # [sg.Text('Train :'), sg.Text(size=(15, 1), key='-TRAIN_STATUS-', font='Any 15', text_color='#5990F6'), ],
            [sg.Text('Nama :'), sg.Text(size=(15, 1), key='-OUT_NAMA-', font='Any 15', text_color='#5990F6'), ],
            [sg.Input(key='-IN_NAMA-')],

            [sg.Button('Tambah Data', font='Any9', button_color='#5990F6'),
             sg.Button('TRAIN', font='Any9', button_color='#5990F6'),]
        ]
    ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(800, 400))

    cap = cv2.VideoCapture(0)
    # variabel cap untuk dapat mencari index webcam secara automatis

    cap.set(3, 300)
    # cap.set(4, 400)

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()

        if event == 'Tambah Data':
            window['-OUT_NAMA-'].update(values['-IN_NAMA-'])
            # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            nama = values['-IN_NAMA-']
            foto(nama, frame)
            print(nama)
        if event == 'TRAIN':
            train()
            print('train')
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    window.close()
