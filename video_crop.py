import cv2
import os
import lista_musicas

#for file in os.listdir("videos"):
  
file = os.listdir("videos")

musica = lista_musicas.musicas[0].replace(" ","")
vidcap = cv2.VideoCapture(musica)
print(vidcap)
success,image = vidcap.read()
success = True
count = 0
filename = "./frames/"+musica+"/"+musica+"%d.jpg" % count

if vidcap.isOpened():
  print(filename)
  while success:
    cv2.imwrite("./teste/%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  print('Read a new frame: ', success)
  count += 1
  cap.release()