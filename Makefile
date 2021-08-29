clean:
	rm -rf dist/

dist:

pytest:
	micropython test/test_ferris_wheel_config.py

.PHONY:
	pytest