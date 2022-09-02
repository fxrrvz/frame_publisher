import re
import sys
import argparse
import lista_musicas
import cv2
import os

def extractImages(filename, pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    dir = "C:/frame_publisher/frames/"+filename
    if not os.path.exists(dir):
        os.makedirs(dir)
    #success,image = vidcap.read()
    #print(success, frame)
    
    if not vidcap.isOpened():
        print("Falha isopened")
        exit()
    while True:
        arquivo = dir +'/' + filename + '%d.png' % count
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        ret, frame = vidcap.read()
        
        while ret == False:
            print("while ret false")
            vidcap.release()
            vidcap = cv2.VideoCapture(pathIn)
            ret, frame = vidcap.read()

        cv2.imwrite(arquivo, frame)     # save frame as JPEG file
        count = count + 1