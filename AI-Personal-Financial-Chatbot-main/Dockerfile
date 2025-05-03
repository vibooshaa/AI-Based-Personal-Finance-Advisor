# Use official slim Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into the container
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Command to run Streamlit app on all interfaces
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
