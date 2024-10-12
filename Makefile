.PHONY: all typing black isort

all: typing black isort

typing:
	poetry run pyright BASIC/ INTERMEDIATE/

black:
	poetry run black BASIC/ INTERMEDIATE/

isort:
	poetry run isort BASIC/ INTERMEDIATE/