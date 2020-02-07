FROM python:3.8-alpine

ENV USER package_user
RUN adduser -D $USER

RUN apk add --no-cache gcc libc-dev unixodbc-dev libffi-dev

COPY requirements/production.txt /tmp/requirements/production.txt
RUN pip install setuptools pip --upgrade && \
    pip install --no-cache -r  /tmp/requirements/production.txt && \
    rm /tmp/requirements/production.txt


COPY dist /tmp/dist
RUN pip install --no-cache /tmp/dist/* && rm -r /tmp/dist

USER $USER

WORKDIR /opt/project
COPY run_service.py run_servicer.py


EXPOSE 8085

CMD ["python", "run_servicer.py", "--port", "8085"]
