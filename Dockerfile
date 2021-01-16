FROM ubuntu:latest

RUN apt-get update && \
	apt-get install -y python3 \
					   python3-pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

EXPOSE 5001
ENTRYPOINT ["python"]
CMD ["main.py"]
