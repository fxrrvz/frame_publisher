import lista_musicas
import video_crop

if __name__=="__main__":
    filename = lista_musicas.musicas[0]
    pathOut = filename+".png"
    pathIn = r'C:/frame_publisher/videos/'+filename+'.mp4'

    video_crop.extractImages(filename, pathIn, pathOut)