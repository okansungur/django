FROM python:3.9.10-alpine

# working directory
WORKDIR /usr/src/myapp

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install necessary  dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/myapp
RUN pip install -r requirements.txt

# copy project folders
COPY . /usr/src/myapp

# define port
EXPOSE 8000

# run myapp
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]