FROM python:3.6.4

COPY ./ /app/

WORKDIR /app

RUN . ./env_var.sh

CMD bash -c "pip3 install -r ./requirements.txt && sh setup.sh heroku"
