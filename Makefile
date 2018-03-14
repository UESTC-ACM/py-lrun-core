host-test:
	@vagrant ssh -c "cd /vagrant/; make test"

test:
	@python2.7 test.py

clean:
	rm -rf *.log
	rm -rf tests/test_case[0-9]/*.class
	rm -rf tests/test_case[0-9]/*.bin
	rm -rf tests/test_case[0-9]/user.out
