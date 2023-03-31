FROM python:3.10-slim 
ADD . .
RUN apt-get update \ 
&& apt-get install -y --no-install-recommends git \ 
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
EXPOSE 8220 80 443 3001
ENTRYPOINT ["streamlit","run"] 
CMD ["./GPT.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=8220","--server.address=0.0.0.0"]