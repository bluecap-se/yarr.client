
install:
	@pip install --pre -r requirements.txt
	@pip install -e .

test:
	@nosetests

serve:
	@python run.py


.PHONY: install test serve
