FROM python:3.10 
ADD . .
RUN pip install -r requirements.txt
EXPOSE 8220
ENTRYPOINT ["streamlit","run"] 
CMD ["./GPT.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=8220","--server.address=0.0.0.0"]