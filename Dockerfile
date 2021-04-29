FROM python:3.6

WORKDIR /

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /

CMD [ "python", "app.py" ]