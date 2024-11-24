FROM python:3.9

WORKDIR /app

COPY . .

RUN make prod

# Exposure of the 5000 port
EXPOSE 5000

CMD ["make", "run"]