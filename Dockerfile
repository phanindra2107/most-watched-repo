FROM ubuntu:18.04
MAINTAINER "phanindra2107@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -sf /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip install requests
COPY ./repos-list.py /usr/bin/
RUN chmod 777 /usr/bin/repos-list.py
CMD python /usr/bin/repos-list.py -t $ENV1 -d $ENV2
ENTRYPOINT ["python", "/usr/bin/repos-list.py"]
#ENTRYPOINT ["python3"]
#ENTRYPOINT ["/usr/bin/repos-list.py", "run"]
