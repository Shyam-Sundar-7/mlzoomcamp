FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["predict.py","lgb_model.bin","standardscaler.bin", "./"]

RUN apt-get update && apt-get install -y libgomp1

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696","predict:app"]