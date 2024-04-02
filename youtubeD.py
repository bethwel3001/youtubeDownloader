# import pafy
from flask import Flask, render_template,request
from pytube import YouTube
# import moviepy.editor
# .....................

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexx.html")

@app.route("/download", methods=["POST"])


# ......................

def download_youtube_media():
    try:
        link = input("Paste the YouTube video link: ")
        
        video = YouTube(link)
        audio = YouTube(link)
        
        # Ask user for choice (audio or video)
        choice = input("Do you want to download audio (A) or video (V)? ").lower()

            #..............Video Download...........
             # best_video = video.getbest() 
             # # Choose the best video stream
        if choice == 'v':
            streams = video.streams
            stream = video.streams.get_highest_resolution()
            # best_video.download()
            stream.download()
            print("Video downloaded successfully!")
            
              # ...........Audio Download...........(a)
              # Choose the best audio stream

        elif choice == 'a':
            
            # video = moviepy.editor.VideoFileClip('filename')
            # audio = video.audio
            # audio.write_audiofile('filename.mp3')
            # audiostreams = video.audiostreams
            # best_audio = audiostreams[0]  
            # best_audio.download()
                          # audio
                      # link to audio playlist: https://youtu.be/taYQKvVu92k    
            streams = audio.streams
            streams = audio.streams.get_highest_resolution()
            stream.download()
            
            print("Audio downloaded successfully!")
            
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_youtube_media()
