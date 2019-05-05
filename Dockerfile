FROM debian

ARG UNAME=testusr
ARG UID=2002
ARG GID=2002

RUN apt-get update -y && apt-get install apt-utils python python-pip nano -y && pip install psutil && apt-get clean

RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

USER $UNAME

ADD sysmon.py /home/$UNAME/sysmon.py

WORKDIR /home/$UNAME

ENTRYPOINT ["python", "sysmon.py"]