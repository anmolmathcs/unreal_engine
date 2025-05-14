import streamlit as st
import openai
from modules.llm_generator import generate_script
from modules.audio_generator import generate_audio
from modules.sequence_editor import modify_sequence
from modules.lipsync_handler import apply_lipsync
from modules.video_renderer import render_video
from config import OPENAI_API_KEY

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
    st.session_state.final_script = None

st.title("🎭 Unreal Video Generator for your character")

# User input box
user_prompt = st.text_area("Enter your prompt:", "")

if st.button("Generate Script"):
    if user_prompt:
        script = generate_script(user_prompt)
        st.session_state.history.append(script)
        st.session_state.final_script = script
    else:
        st.warning("Please enter a prompt.")

# Show generated script history
if st.session_state.history:
    st.subheader("Generated Scripts")
    for i, script in enumerate(st.session_state.history):
        st.write(f"**Version {i+1}:**")
        st.text_area("", script, height=200, key=f"script_{i}")

    # Allow modifications
    if st.session_state.final_script:
        modified_script = st.text_area("Modify the final script if needed:", st.session_state.final_script)
        if st.button("Confirm Script"):
            st.session_state.final_script = modified_script
            st.success("Script confirmed!")

# Trigger full pipeline
# if st.session_state.final_script and st.button("Generate Video"):
#     with st.spinner("Generating audio..."):
#         audio_file = generate_audio(st.session_state.final_script)
    
#     sequence_path = "/Game/Sequences/BaseSequence"
#     with st.spinner("Modifying Unreal sequence..."):
#         modify_sequence(sequence_path, audio_file)
    
#     with st.spinner("Applying lipsync..."):
#         apply_lipsync(sequence_path, audio_file)
    
#     with st.spinner("Rendering video..."):
#         render_video(sequence_path)
    
#     st.success("Video generation complete!")
