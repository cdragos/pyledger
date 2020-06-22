# Using a python image with a pre-compiled pandas on the Alpine platform
# to avoid long building times from pandas source
FROM nickgryg/alpine-pandas:3.8

WORKDIR /var/lib/pyledger

# Copy requirements file and install dependencies.
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

# Copy the application files.
COPY . .

ENV PYTHONIOENCODING utf_8
