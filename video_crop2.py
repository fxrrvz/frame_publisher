import re
import sys
import argparse
import lista_musicas
import cv2
import os

def extractImages(filename, pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    os.makedirs(filename)
    #success,image = vidcap.read()
    #print(success, frame)
    
    if not vidcap.isOpened():
        print("Falha isopened")
        exit()
    while True:
        arquivo = 'C:/frame_publisher/'+filename+'/'+filename+'%d.png'%count
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        ret, frame = vidcap.read()
        
        while ret == False:
            print("while ret false")
            vidcap.release()
            vidcap = cv2.VideoCapture(pathIn)
            ret, frame = vidcap.read()

        cv2.imwrite(arquivo, frame)     # save frame as JPEG file
        count = count + 1   

if __name__=="__main__":
    filename = lista_musicas.musicas[0]
    pathOut = filename+".png"
    pathIn = r'C:/frame_publisher/videos/'+filename+'.mp4'
    extractImages(filename, pathIn, pathOut)



    '''a = argparse.ArgumentParser()
    a.add_argument("videos\\"+lista_musicas.musicas[0], help="path to video")
    a.add_argument(filename, help="path to images")
    args = a.parse_args(1, 2)
    print("aaaaaaaaaaa")
    print(args)
    extractImages(args.pathIn, args.pathOut)
    '''