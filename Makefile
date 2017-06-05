test:
	python2.7 test.py

clean:
	rm -rf *.log
	rm -rf tests/test_case[0-2]/*.class
	rm -rf tests/test_case[0-2]/*.bin
	rm -rf tests/test_case[0-2]/user.out
