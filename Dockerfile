FROM python:3.10-alpine
WORKDIR /pythonApp
COPY dependency.txt /pythonApp
RUN pip install -r dependency.txt --no-cache-dir
COPY . /pythonApp
CMD python app.py
