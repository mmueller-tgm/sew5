from jenkins/jenkins:lts

USER root

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install pylint
RUN apt-get install python3-nose python3-coverage -y

USER jenkins

EXPOSE 8080
