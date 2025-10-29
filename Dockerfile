FROM python:3.13

# Install pipenv globally
RUN pip install pipenv

WORKDIR /app

COPY . /app/

RUN pipenv install
