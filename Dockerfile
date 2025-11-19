FROM python:3.10-slim

# Install build dependencies for llama-cpp-python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the repo
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["python", "app.py"]
