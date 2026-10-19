import streamlit as st

st.title("YouTube to Shorts Generator")
st.write("Apni YouTube video ka link neeche paste karen:")

url = st.text_input("YouTube Video URL")

if st.button("Generate Shorts"):
    if url:
        st.success(f"Processing video: {url}")
        st.info("AI video ko analyze kar raha hai...")
    else:
        st.warning("Kharab link! Barae meherbani sahi YouTube URL daalein.")
