# Builder stage
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt --no-cache-dir --use-pep517

# Operational stage
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Get the virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

COPY . .

CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--access-logformat", "%(h)s %(l)s \"%(r)s\" %(s)s Origin:\"%({origin}i)s\" X-Forwarded-For:\"%({x-forwarded-for}i)s\""]