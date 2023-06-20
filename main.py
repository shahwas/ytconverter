import streamlit as st
from pytube import YouTube
import moviepy.editor as mp

def download_mp3_and_mp4(url):
    try:
        # Download the YouTube video
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video_filename = video.default_filename
        video.download()

        # Convert the downloaded video to MP3
        mp4_file = video_filename
        mp3_file = video_filename.split('.')[0] + '.mp3'
        video_clip = mp.VideoFileClip(mp4_file)
        video_clip.audio.write_audiofile(mp3_file)

        return mp3_file, mp4_file

    except Exception as e:
        print("Error occurred while downloading and converting:", str(e))

def main():
    st.title("YouTube MP3 and MP4 Downloader")
    st.write("Enter a YouTube URL to download and convert the video")

    # Get the YouTube URL from the user
    url = st.text_input("Enter the YouTube URL")

    if st.button("Download and Convert"):
        if url:
            # Download and convert the video
            mp3_file, mp4_file = download_mp3_and_mp4(url)

            if mp3_file and mp4_file:
                st.success("Download and conversion completed successfully!")

                # Display the MP3 file with a download button
                st.audio(mp3_file, format='audio/mp3')
                st.download_button("Download MP3", data=mp3_file, file_name=mp3_file)

                # Display the MP4 file with a download button
                st.video(mp4_file)
                st.download_button("Download MP4", data=mp4_file, file_name=mp4_file)

if __name__ == '__main__':
    main()
