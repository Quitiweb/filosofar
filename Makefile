SHELL := /bin/bash

install:
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

start_django_server:
	source .venv/bin/activate && python manage.py runserver

run_streamlit:
	source .venv/bin/activate && streamlit run st_dashboard.py

init_database:
	source .venv/bin/activate && python manage.py migrate
	source .venv/bin/activate && DJANGO_SUPERUSER_PASSWORD=temporal2022 python manage.py createsuperuser --noinput --username admin --email admin@admin.com
	make load_data

load_data:
	source .venv/bin/activate && python manage.py load_coin_data
