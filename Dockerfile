# Export peotry requirements
FROM python:3.11-alpine as poetry_installer

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Build image
FROM python:3.11-alpine

WORKDIR /app

COPY --from=poetry_exporter /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "<project_name>/server.py"]