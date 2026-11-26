# Training baseline: intentionally not hardened.
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
RUN useradd --create-home --uid 10001 --user-group appuser
      USER 10001:10001
EXPOSE 5000

CMD ["python", "app.py"]
