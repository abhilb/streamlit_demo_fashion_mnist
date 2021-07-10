import streamlit as st
import tensorflow as tf
import logging
import numpy as np

logger = logging.getLogger()
logging.basicConfig(loglevel=logging.INFO)

@st.cache
def download_dataset():
    logger.info("download dataset")
    return tf.keras.datasets.fashion_mnist.load_data()

def main(data):

    st.title("Fashion MNIST classification demo")
    img_placeholder = st.empty()
    txt_placeholder = st.empty()

    idx = 0

    if st.button('Next Image'):
        idx = np.random.randint(0, len(data))

    img = data[idx, :, :]
    img_placeholder.image(img, width=200)

    prediction = "Unknown"
    txt_placeholder.text(prediction)


if __name__ == '__main__':
    (train_data, train_target), (test_data, test_target) = download_dataset()
    main(test_data)
