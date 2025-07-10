FROM python:3.13.3-slim

WORKDIR /abc

# Install Poetry
RUN pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir poetry==2.1.2

COPY pyproject.toml poetry.lock ./

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --without dev --no-cache --no-root --no-interaction --no-ansi

COPY . .

CMD [ "python", "app/main.py" ]