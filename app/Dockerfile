# start by pulling the python image
FROM python:3

RUN apt-get update
RUN apt-get install -y --no-install-recommends


# set working directory
WORKDIR /app

# install required libraries
COPY requirements.txt .
RUN pip install -U -r requirements.txt

# copy source code into working directory
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]