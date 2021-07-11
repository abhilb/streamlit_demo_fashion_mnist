FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 && apt-get install -y git && apt-get install -y python3-pip

WORKDIR /usr/src/app

RUN git clone https://github.com/abhilb/streamlit_demo_fashion_mnist.git

WORKDIR /usr/src/app/streamlit_demo_fashion_mnist

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install cython

RUN python3 -m pip install streamlit

RUN python3 -m pip install tensorflow

EXPOSE 8501

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

CMD ["streamlit", "run", "./main.py"]
