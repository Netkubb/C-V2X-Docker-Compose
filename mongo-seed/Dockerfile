# Use an official Python image
FROM python:3.10-slim

# Set environment variables to avoid Python buffer issues
ENV PYTHONUNBUFFERED=1

# Install necessary Python packages
RUN pip install pymongo

# Set the working directory in the container
WORKDIR /app

# Copy the seed.py script into the container
COPY seed.py .

# Command to execute the seeding script
CMD ["python", "seed.py"]