#
# executive file runner for compiled source code by compiler.
#
from os import path
import commands
import util
import lrun


running_argument = "lrun --max-cpu-time {cpu_time} --max-real-time {real_time} " \
                   "--max-memory {memory} --network false --remount-dev true --reset-env true " \
                   "--syscalls '{blacklist}' --max-nprocess 20 {command} < {input_file} > " \
                   "{user_output_file} 3>&2"
user_output_file = "user.out"


def Judge(input_file, std_output_file, user_output_file, spj = False):
    if spj:
        pass
    else:
        pass
    return True


def Run(language_token, source_file, cpu_time, real_time, memory, data_dir, test_case, work_dir):
    work_dir = path.abspath(work_dir)
    running_command = util.judge_languages[language_token]["executive_command"] \
                          .format(source_file = source_file, work_dir = work_dir)
    blacklist = util.judge_languages[language_token]["blacklist"]
    input_file = path.abspath(data_dir + "/" + test_case + ".in")
    output_file = path.abspath(work_dir + "/" + user_output_file)
    status, output = commands.getstatusoutput(running_argument.format(cpu_time = cpu_time, \
                                                                      real_time = real_time, \
                                                                      memory = memory, \
                                                                      blacklist = blacklist, \
                                                                      command = running_command, \
                                                                      input_file = input_file, \
                                                                      user_output_file = output_file))

    pivot = output.rfind("MEMORY   ")
    if pivot == -1:
        return "SE"
    if pivot:
        lrun_error = output[ : pivot]
    else:
        lrun_error = None
    result = lrun.Parse(output[pivot : ])

    if result["EXCEED"] != "none":
        if result["EXCEED"] == "memory":
            return "MLE"
        elif result["EXCEED"] in ["cpu_time", "real_time"]:
            return "TLE"
        else:
            return "SE"
    if result["EXITCODE"] != "0" or result["SIGNALED"] != "0" \
       or result["TERMSIG"] != "0" or lrun_error:
        return "RE"

    if Judge(test_case + ".in", test_case + ".out", user_output_file):
        return "AC\n" + str(result)
    else:
        return "WA"
