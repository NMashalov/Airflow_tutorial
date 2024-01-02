FROM apache/airflow:2.6.1
ADD airflow_requirements.txt .
RUN apt-get update \
  && apt-get -y install wget ghostscript tesseract-ocr tesseract-ocr-rus 

RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt