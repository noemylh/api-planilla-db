#!/bin/sh

yum update -y
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y gcc gcc-c++ glibc-langpack-en bzip2-devel wget curl vim make telnet python3 python3-devel

# Prepare environment to be able to create PDFs from HTML templates
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.centos8.x86_64.rpm
yum install -y libXrender fontconfig urw-fonts libXext libtiff libpng15
yum localinstall -y wkhtmltox-0.12.6-1.centos8.x86_64.rpm

# Set environment variables for SQL Server libraries to work
echo $'\n\nUpdate BashRC'
echo 'export TDSVER=7.3' >> ~/.bashrc
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc

## Install Python libraries
echo $'\n\nInstall Python libraries'
pip3 install --upgrade pip
pip3 install flask==1.1.1 gunicorn==19.9.0 python-dotenv==0.12.0 requests==2.22.0 cryptography==2.9.2 pyOpenSSL==19.0.0 pyYAML==5.3.1 pandas==0.25.1 openpyxl==3.0.4 cython==0.29.17 python-pdf pdfkit==0.6.1 validator==0.7.0
pip3 install pyodbc==4.0.30 xlrd==1.2.0 flask==1.1.1 paramiko==2.6.0 python-gnupg==0.4.6 sendgrid==6.3.1 Pillow==6.1.0
pip3 install pybase64==1.2.2
pip3 install bcrypt==3.2.2 flask-pymongo==2.3.0

echo $'\n\nRemove temporary files'
rm -Rf Dockerfile createImage.sh requirements.sh .git wkhtmltox-0.12.6-1.centos8.x86_64.rpm