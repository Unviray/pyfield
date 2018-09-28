clean:
	@echo Cleaning up
	rm -rf .tox *.egg dist build .coverage
	find . -name '__pycache__' -delete -o -name '*.pyc' -delete
	@echo
