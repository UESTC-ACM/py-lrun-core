#
# Integration test cases.
#
import traceback
import compiler
import runner


def RunTest(test_case_file):
    fp = open("tests/" + test_case_file + "/config", "r")
    assert fp != None
    work_dir = "tests/" + test_case_file
    passed = True
    try:
        for line in fp:
            wrapped = line.strip()
            if not wrapped:
                continue
            language_token, source_file, time, memory, data, expected = wrapped.split(" ")
            compiler.Compile(language_token = language_token, \
                             source_file = source_file, \
                             work_dir = work_dir)
            actual = runner.Run(language_token = language_token, \
                                source_file = source_file, \
                                cpu_time = int(time) / 1000.0, \
                                real_time = int(time) / 1000.0 * 2, \
                                memory = int(memory) * 1024 * 1024, \
                                test_case = data, \
                                data_dir = work_dir, \
                                work_dir = work_dir)
            assert actual.startswith(expected), \
                "test case'%s': expected answer is %s but actual answer is %s." \
                % (wrapped, expected, actual)
    except:
        traceback.print_exc()
        passed = False
    finally:
        fp.close()
    if passed:
        print "testing " + test_case_file + " \033[0;32mPASSED\033[m"
    else:
        print "testing " + test_case_file + " \033[0;31mFAILED\033[m"

RunTest("test_case0")
RunTest("test_case1")
