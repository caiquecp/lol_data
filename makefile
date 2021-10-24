format:
	black -l 120 lol_data

check-typing:
	mypy lol_data

run:
	python -m lol_data