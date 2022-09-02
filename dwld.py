import lista_musicas
import YTDL
import asyncio
import os
import urllib.parse, urllib.request, re
from urllib.request import urlopen, FancyURLopener
from urllib.parse import urlparse, parse_qs, unquote

def pesquisa(search: str, ):
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
    print(query_string)
    url = 'http://www.youtube.com/watch?v=' + search_results[0]
    return url


######################################################################################


musicas = lista_musicas.musicas
url = pesquisa(musicas[0])
filename = re.sub
f = '-o ./videos/'+musicas[0]+'.mp4 ' 
#player = YTDL.YTDLSource.from_url(url)

os.system('youtube-dl '+f+url)

#print(player)