# ================= Builder Stage =================
FROM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --prefix=/install


# ================= Runtime Stage =================
FROM python:3.12.1-slim

WORKDIR /app

# Copy only runtime dependencies
COPY --from=builder /install /usr/local

# Copy application code
COPY app.py .

# Run as non-root user
RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]
