# Базовый образ
FROM python:3.9-slim

# Установка зависимостей
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/sqz1337/baltic_alfa_hack_2023 .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта в образ
COPY data data
COPY models models
COPY notebooks notebooks
COPY src src
COPY .gitignore .
COPY README.md .

# Команда запуска приложения
CMD ["python", "src/train_model.py"]