FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["tacl2025_ood_eval_self_rationalization"]
