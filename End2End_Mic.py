# # !pip install bokeh
# # !pip install streamlit_bokeh_events
# import streamlit as st
# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events

# stt_button = Button(label="Speak", width=100)

# stt_button.js_on_event("button_click", CustomJS(code="""
#     var recognition = new webkitSpeechRecognition();
#     recognition.continuous = true;
#     recognition.interimResults = true;
 
#     recognition.onresult = function (e) {
#         var value = "";
#         for (var i = e.resultIndex; i < e.results.length; ++i) {
#             if (e.results[i].isFinal) {
#                 value += e.results[i][0].transcript;
#             }
#         }
#         if ( value != "") {
#             document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
#         }
#     }
#     recognition.start();
#     """))

# result = streamlit_bokeh_events(
#     stt_button,
#     events="GET_TEXT",
#     key="listen",
#     refresh_on_update=False,
#     override_height=75,
#     debounce_time=0)

# if result:
#     if "GET_TEXT" in result:
#         st.write(result.get("GET_TEXT"))



# !pip install audio-recorder-streamlit
import streamlit as st
# from audiorecorder import audiorecorder
from audio_recorder_streamlit import audio_recorder

st.title("Audio Recorder")
# audio = audiorecorder("Click to record", "Click to stop recording")
audio = audio_recorder(pause_threshold=2.0, sample_rate=41_000)
st.audio(audio)


# if len(audio) > 0:
#     # To play audio in frontend:
#     st.audio(audio.export().read())  

#     # To save audio to a file, use pydub export method:
#     audio.export("audio.wav", format="wav")

#     # To get audio properties, use pydub AudioSegment properties:
#     st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

