FROM bitnami/spark:3.5.6

# Switch to root to install packages and set up directories
USER root

# Install required packages
RUN apt-get update && \
    apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/spark-app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONPATH="${PYTHONPATH}:/opt/bitnami/spark/python:/opt/bitnami/spark/python/lib/py4j-0.10.9.7-src.zip"
ENV PYTHONUNBUFFERED=1


