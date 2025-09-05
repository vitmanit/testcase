1) Применяем миграцию docker-compose exec web alembic upgrade head
2) Всё работает. 


Если же не видит миграцию 
1) Сначала создаём её: docker-compose exec web alembic revision --autogenerate -m "create tables"
2) Затем применяем: docker-compose exec web alembic upgrade head
