import os, openai, time, whisper
import gradio as gr 
from audiorecorder import audiorecorder
from dotenv import load_dotenv
load_dotenv() 
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
#Gradio inputs 
#2 dropdown menus, 1 textbox, 1 process button 
gr_inputs = [gr.Textbox('Write down your prompt'), 
             gr.Dropdown(styleList,label='Choose A Style'), 
             gr.Dropdown(langList,label='Choose A Language')] 
gr_output = gr.Textbox(label='GPT Output') 

#Incomplete for testing reasons
def gradio_main(prompt, style,language,audio): 
    if audio != None: 
        result = whisper_model.transcribe(audio)['text']
        print(result) 
        return chatGPT("Use the "+language+" when answering the following question: "+result)
    elif style == 'Plagiarism Checker': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Check the following text for plagiarism: "+prompt)
    elif style == 'Shakespearean Response': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Rewrite the following text in a Shakespearean way: "+prompt)
    elif style == 'Python Interpreter': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Write a Python program that performs the following description: "+prompt)
    elif style == 'Java Code Generation': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Write a Java program that performs the following description: "+prompt)
    elif style == 'Music Suggestions': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Suggest songs similar to the given song: "+prompt)
    elif style == 'Hackathon Idea Generator': 
        return chatGPT("Use the "+language+" when answering the following question: "+"Generate five ideas based on this theme: "+prompt)
    else: 
        return chatGPT(prompt)


with gr.Blocks() as demo:
    gr_inputs = [
             gr.Textbox(), 
             gr.Dropdown(styleList,value='None',label='Choose A Style'), 
             gr.Dropdown(langList,value='English',label='Choose A Language'), 
             gr.Audio(source="microphone",type="filepath")
             ] 
    gr_output = gr.Textbox(label='GPT Output') 
    button = gr.Button(value='Process')
    button.click(gradio_main,inputs=gr_inputs,outputs=gr_output)

demo.launch(share=True)

