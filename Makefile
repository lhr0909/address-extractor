serve:
	poetry run uvicorn api.main:app --host 0.0.0.0 --port 7000 --reload --reload-dir api