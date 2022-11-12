import streamlit as st
st.title("Welcome to the side tasks")
st.header("3taTLNS")
st.subheader("Details")
st.markdown("""
```
http://127.0.0.1:5000/
~/exun_22
```
""")
hide_streamlit_style = "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)