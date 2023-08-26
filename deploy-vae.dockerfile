FROM python:3.9-slim

RUN apt-get update
RUN apt-get install -y openssl
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --upgrade --no-cache-dir pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --upgrade google-cloud-vision
RUN pip install --upgrade azure-cognitiveservices-vision-computervision

COPY ./autoencoder.model /code/autoencoder.model
COPY ./damaged_img.jpeg /code/damaged_img.jpeg
COPY ./good_img.jpeg /code/good_img.jpeg
COPY ./test_vae.py /code/test_vae.py

ENTRYPOINT ["python3", "test_vae.py"]