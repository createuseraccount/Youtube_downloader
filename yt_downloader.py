from pytube import YouTube
from pytube import Playlist
import argparse,os

def videos_download(url,qualty):
    print("->Starting Youtube video list downloading")
    no = 1
    lnks = []
    target_playlist = Playlist(url)
    for i in target_playlist.parse_links():
        lnk = "https://www.youtube.com"+i
        yt = YouTube(lnk)
        print(str(no),")",yt.title,lnk)
        lnks.append(lnk)
        no = no + 1
    print("\n")

    for i in lnks:
        if qualty == '360':
            yt = YouTube(i)
            st = yt.streams.get_by_itag('43')
            try:
                st.download()
                print("[+]",yt.title," was downloaded(360p)")
            except:
                print("[-]",yt.title,"couldnt downloaded(360p)")

        elif qualty == '720':
            yt = YouTube(i)
            st = yt.streams.get_by_itag('22')
            try:
                st.download()
                print("[+]",yt.title," was downloaded(720p)")
            except:
                print("[-]",yt.title,"couldnt downloaded(720p)")


def video_download(video,qualty):
    print("->Starting Youtube video downloading")
    yt = YouTube(video)
    if qualty == '360':
        st = yt.streams.get_by_itag('43')
        st.download()
        print("[+]",yt.title," was downloaded(360p)")
    elif qualty == '720':
        st = yt.streams.get_by_itag('22')
        st.download()
        print("[+]",yt.title," was downloaded(720p)")

def downloading_size():
    files = os.listdir(os.getcwd())
    file_size = 0
    for i in files:
        if i.endswith('.webm'):
            file_size += os.path.getsize(i)

    if file_size < 1024:
        print(round(file_size), "Bayt")
    elif 1024 <= file_size < 1024**2:
        print(round(file_size / 1024), "KB")
    elif 1024**2 <= file_size < 1024**3:
        print(round(file_size / (1024 * 1024)), "MB")
    elif 1024**3 <= file_size < 1024**4:
        print(round(file_size / (1024*1024*1024)), "GB")

def main():
    parser =argparse.ArgumentParser()
    parser.add_argument("--lst","-l",help="download for list")
    parser.add_argument("--video","-v",help="download for just a video")
    parser.add_argument("--qualty","-q",help="videos qualty")
    data = parser.parse_args()

    if data.lst is not None:
        videos_download(data.lst,data.qualty)

    elif data.video is not None:
        video_download(data.video,data.qualty)

    downloading_size()

if __name__ == '__main__':
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'Linux':
        os.system("clear")

    main()