import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Free YouTube Shorts Generator", layout="centered")

st.title("🎬 YouTube to Shorts Generator")
st.write("Apni YouTube video ka link paste karen, hum us me se aapko clips process karke denge.")

url = st.text_input("YouTube Video URL Here:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Shorts Clips"):
    if url:
        st.info("⏳ Video fetch ho rahi hai... Baraye meherbani thoda intezar karen.")
        
        # Updated options to bypass 403 Forbidden error
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': 'downloaded_video.mp4',
            'overwrites': True,
            'geo_bypass': True,
            'nocheckcertificate': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            st.success("✅ Video successfully download ho gayi hai!")
            
            # Show original video preview
            if os.path.exists("downloaded_video.mp4"):
                st.video("downloaded_video.mp4")
                st.info("💡 Next step: AI script analysis & short video cutting.")
                
        except Exception as e:
            st.error(f"Error aaya hai: {str(e)}")
    else:
        st.warning("⚠️ Pehle koi YouTube link enter karan!")
