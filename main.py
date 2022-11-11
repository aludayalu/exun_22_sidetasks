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
st.markdown("""
<audio controls><source src="http://127.0.0.1:5000/house.ogg" type="audio/ogg" id="bgAudio">
Your browser does not support the audio element.
</audio>
<plaintext>   ^^^ For vibing (loud) 😋</plaintext>
<script>
  var audio = document.getElementById("bgAudio");
  audio.volume = 0.1;
</script>
""",unsafe_allow_html=True)
hide_streamlit_style = "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)