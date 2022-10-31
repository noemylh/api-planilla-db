FROM quay.io/centos/centos:stream8

WORKDIR /usr/src/app
COPY . .

# Set environment variables for SQL Server libraries to work
RUN source /usr/src/app/requirements.sh

EXPOSE 443
CMD ["gunicorn", "-b", "0.0.0.0:443", "--timeout", "300", "--workers", "4", "main:app"]
#CMD ["python3","main.py"]
