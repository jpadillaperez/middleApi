FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install pymongo
RUN pip install python-dotenv
EXPOSE 5000
CMD ["python3", "app.py"]