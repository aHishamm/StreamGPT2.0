import os
import openai
import time
import whisper
import streamlit as st 
from audiorecorder import audiorecorder
from dotenv import load_dotenv
load_dotenv() 
st. set_page_config(layout="wide")
whisper_model = whisper.load_model("base") 
openai.api_key = os.getenv("OPENAI_API_KEY")
def chatGPT(userinput,temperature=0,max_tokens=1000): 
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', 
        messages= [{"role":"user","content":userinput}],
        temperature=temperature, 
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']
#Example Styles I came up with 
styleList = ['None','Plagiarism Checker','Shakespearean Response','Python Interpreter','Java Code Generation','Music Suggestions','Hackathon Idea Generator']
#Language selector options 
langList = ['Arabic','English','Italian','German','Hebrew','Russian','Urdu','Hindi'] 
colsec, col1, col2 = st.columns(3) 
with colsec: 
    #temperature and max_tokens sliders 
    temperature = st.slider('The higher the temperature, the more random the response',0.0,2.0,0.0)
    max_tokens = st.slider('Maximum number of tokens that ChatGPT will generate as a response',100,2500,100)
    audio_bytes = audiorecorder("Click to record","Recording...") 
    if len(audio_bytes > 0): 
        st.audio(audio_bytes.tobytes())
        wav_file = open("audio.mp3", "wb")
        wav_file.write(audio_bytes.tobytes()) 
        model = whisper.load_model("base")
        result = model.transcribe(wav_file.name)
        print(result['text'])
        st.write(result['text'])
        res = chatGPT(result['text'],temperature,max_tokens)
with col1: 
    style_option = st.selectbox("Choose a style: ",styleList)
    lang_option = st.selectbox("Choose a language: ",langList)
    if style_option == 'Plagiarism Checker': 
        user_input = st.text_input("Write the text you want to check for plagiarism: ")
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Check the following text for plagiarism: "+user_input,temperature,max_tokens) 
    elif style_option == 'Shakespearean Response': 
        user_input = st.text_input("Write the text you want to be rewritten in a Shakespearean way: ")
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Rewrite the following text in a Shakespearean way: "+user_input,temperature,max_tokens)
    elif style_option == 'Python Interpreter': 
        user_input = st.text_input("Write down the coding problem: ")
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Write a Python program that performs the following description: "+user_input,temperature,max_tokens)
    elif style_option == 'Java Code Generation': 
        user_input = st.text_input("Write down the coding problem: ") 
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Write a Java program that performs the following description: "+user_input,temperature,max_tokens)
    elif style_option == 'Music Suggestions': 
        user_input = st.text_input("Write down the name of the song and the artist who performed it: ") 
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Suggest songs similar to the given song: "+user_input,temperature,max_tokens) 
    elif style_option == 'Hackathon Idea Generator': 
        user_input = st.text_input("Write down the theme you want ideas for: ")
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+"Generate five ideas based on this theme: "+user_input,temperature,max_tokens)
    else: 
        user_input = st.text_input("Ask ChatGPT anything :) ")
        if user_input: 
            res = chatGPT("Use the "+lang_option+" when answering the following question: "+user_input,temperature,max_tokens)
with col2: 
    if user_input or st.button("Process"): 
        with st.spinner('Processing...'): 
            time.sleep(1)
        st.write("ChatGPT Response: ")
        st.write(res)
        st.success("Response Received!",icon="✅")