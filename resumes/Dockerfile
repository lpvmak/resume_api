FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod 766 -R /app
RUN chmod +x entrypoint.sh
RUN chmod +x entrypoint_test.sh
CMD mkdir /static
CMD chmod 766 -R /static
CMD ["./entrypoint.sh"]