FROM apache/airflow:2.8.0
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user "apache-airflow==2.8.0" -r /requirements.txt