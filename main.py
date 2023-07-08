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
        filepath = DIR + author + ' - ' + title + '.mp4'
        os.rename(out_file, filepath)

        print('Downloaded')
    except:
        print('Failed to download song')

if __name__ == '__main__':
    print('Enter 0 to exit')
    link = ''
while (link != '0'):
        print('Paste youtube link: ')
        link = input('>> ')
        download_song(link)
