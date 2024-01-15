# Use the official Python image as base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /streamlit_chat

# Copy and install Python dependencies
COPY requirements.txt /streamlit_chat/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY . /streamlit_chat

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the application on localhost:8501
CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
