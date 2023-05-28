from pytube import YouTube
import os

DIR = '/home/petar/Music/'

def download_song(url):
    video = YouTube(url)
    title = video.title
    author = video.author
    audio = video.streams.filter(only_audio=True).first()
    try:
        out_file = audio.download(DIR)
        base, ext = os.path.splitext(out_file)
        filepath = DIR + author + ' - ' + title + '.mp3'
        os.rename(out_file, filepath)
        
        print(base, '\n', filepath)

        print('Downloaded')
    except:
        print('Failed to download song')

link = 'https://www.youtube.com/watch?v=86PRtZsEv9g'
download_song(link)
