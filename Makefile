clean:
	rm -rf dist/

dist:
	mkdir dist
	python3 bin/compress.py

pytest:
	micropython test/test_ferris_wheel_config.py

.PHONY:
	pytest