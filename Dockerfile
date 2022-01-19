FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 python3-dev python3-setuptools python3-pip curl wget git vim locales dos2unix -y
RUN echo -e '\n\n\n\n\n\n\n\n' | adduser --disabled-password --quiet me  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

COPY *.py /home/me/
COPY runner.sh /home/me/

RUN dos2unix /home/me/runner.sh

USER me
WORKDIR /home/me
ENTRYPOINT [ "./runner.sh" ]