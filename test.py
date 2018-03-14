#
# Integration test cases.
#
import traceback
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
      language_token, source_file, time, memory, data, expected = wrapped.split(
          " ")
      if source_file != "Main":
        continue
      actual = runner.Judge(
          work_dir=work_dir,
          data_dir=work_dir,
          language_token=language_token,
          source_file=source_file,
          time_limit=int(time),
          memory_limit=int(memory),
          test_case=data,
          compile=True)
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
  return passed


passed = True
for i in range(0, 6):
  if not RunTest("test_case" + str(i)):
    passed = False
exit(0 if passed else 1)
