FROM agrigorev/zoomcamp-bees-wasps:v2

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl


COPY function_call.py .



CMD [ "function_call.lambda_handler" ]