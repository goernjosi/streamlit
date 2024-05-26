FROM python:3.12.1

# Copy Files
WORKDIR /usr/app
COPY . .

RUN pip install -r requirements.txt


# Docker Run Command
EXPOSE 5000
CMD ["streamlit", "run",  "streamlit_app.py"]