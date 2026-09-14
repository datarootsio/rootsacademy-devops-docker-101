# Exercise 2 — fill in the blanks. Nothing here runs yet.
#
# 1. Pick an official Python base image.
FROM python:3.12-slim

# 2. Set a working directory inside the image (optional but tidy — everything
#    after this is relative to it).
WORKDIR /app

# 3. Copy requirements.txt in and install it.
#    Order matters: do this BEFORE copying main.py, so editing your code later
#    doesn't force pip to reinstall everything (you'll see why in the next block).
COPY requirements.txt .
COPY src/ ./src
RUN pip install --no-cache-dir -r requirements.txt

# 4. Now copy your source code in.
COPY main.py .

# 5. Tell Docker what to run when the container starts.
#    Exec form — ["python", "main.py"] — not shell form ("python main.py").
ENTRYPOINT ["python", "main.py"]
