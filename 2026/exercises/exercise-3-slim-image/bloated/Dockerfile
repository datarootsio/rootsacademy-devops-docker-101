FROM python:3.12-slim AS builder
RUN apt-get update && apt-get install -y build-essential
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH
WORKDIR /app
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH
COPY main.py .
ENTRYPOINT [ "python", "src.main" ]

# FROM python:3.12

# RUN apt-get update
# RUN apt-get install -y build-essential

# WORKDIR /app
# COPY . .

# RUN pip install -r requirements.txt

# CMD python main.py