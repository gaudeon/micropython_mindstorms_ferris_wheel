clean:
	rm -rf dist/

dist:
	mkdir dist
	python3 bin/compress.py

pytest:
	micropython test/ferris_wheel/test_config.py

.PHONY:
	pytest