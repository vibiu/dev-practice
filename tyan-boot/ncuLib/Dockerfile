FROM centos
MAINTAINER Tyan <tyanboot@outlook.com>
EXPOSE 5000 80
ENV LANG en_US.utf-8
RUN yum install -y https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
RUN yum install -y git wget libpng libpng libtiff libtiff giflib tesseract python34 python-setuptools
WORKDIR /opt
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.4 get-pip.py && rm -f get-pip.py
RUN pip3.4 install requests flask flask-sqlalchemy html5lib BeautifulSoup4 Image pytesseract
WORKDIR /home
COPY . /home/
CMD python3.4 run.py