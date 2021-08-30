setup:
	micropython -m upip install -r requirements.txt

clean:
	rm -rf dist/

dist:
	mkdir dist
	python3 bin/compress.py

pytest:
	micropython test/ferris_wheel/test_config.py
	micropython test/ferris_wheel/test_control.py
	micropython test/ferris_wheel/test_motion.py

.PHONY:
	pytest