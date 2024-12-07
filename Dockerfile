FROM python:3.10
WORKDIR /usr/local/mse-ddm501

# Install application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy main web app's source code
COPY main ./main
COPY models ./models
EXPOSE 6000

# Setup app user
RUN useradd mse_hieunt
USER mse_hieunt
ENV FLASK_RUN_PORT 6500

# Run app
CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]