FROM python:3.9-slim

WORKDIR /Mealmastermind_AIModel/

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn joblib pydantic scikit-learn pandas pymongo python-dotenv

EXPOSE 8000

ENV MODEL_PATH=/Mealmastermind_AIModel/.env.local

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
