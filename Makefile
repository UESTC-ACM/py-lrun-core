host-test:
	@vagrant ssh -c "cd /vagrant/; make test"

test:
	@python2.7 test.py

install:
	LRUN_GROUP=$${USER} make -C lib/lrun install
	make -C lib/comparators install

clean:
	rm -rf *.log
	rm -rf tests/test_case[0-21]/*.class
	rm -rf tests/test_case[0-21]/*.bin
	rm -rf tests/test_case[0-21]/user.out
