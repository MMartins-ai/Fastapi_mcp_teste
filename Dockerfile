FROM python:3.12.3-alpine3.20

WORKDIR /mcp_app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["python3", "mcp_server.py"]