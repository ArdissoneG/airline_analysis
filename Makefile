install:
	pip install -r requirements.txt

extract:
	python src/extract.py

transform:
	python src/transform.py

visualize:
	python src/visualize.py

run:
	python src/main.py

clean:
	rm -f warehouse.db

test:
	pytest tests/