# TestCase API

FastAPI + PostgreSQL + Docker + Alembic
REST API для управления вопросами и ответами. Проект использует:
- **FastAPI** — для создания API
- **PostgreSQL** — в качестве базы данных
- **Docker** — для контейнеризации
- **Alembic** — для миграций БД

 #bash
git clone https://github.com/ваш-пользователь/TestCase.git
cd TestCase

Активируем виртуальное окружение, устанавлвиваем зависимости
pip install -r requirements.txt

Запускаем докер:
- docker-compose up -d --build
Применяем миграции:
- docker-compose exec web alembic upgrade head

Проверяем:
http://localhost:8000/docs
