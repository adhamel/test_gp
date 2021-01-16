FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y python3 \
					   python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py main.py

EXPOSE 5001
ENTRYPOINT ["python3"]
CMD ["main.py"]
