docker build . -t fashion_mnist
docker run -d -p 4000:8501 fashion_mnist
