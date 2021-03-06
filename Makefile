clean:
	@echo Cleaning up
	rm -rf .tox *.egg dist build .coverage
	find . -name '__pycache__' -delete -o -name '*.pyc' -delete
	@echo


doc:
	@echo Building docs
	$(MAKE) -C docs html
	@echo


test:
	@echo Testing
	pipenv run pytest
	@echo

	@echo Linting
	pipenv run pylint pyfield
	@echo
