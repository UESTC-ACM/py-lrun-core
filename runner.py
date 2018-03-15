#
# executive file runner for compiled source code by compiler.
#
from os import path
import commands
import util
import compiler
import lrun
import subprocess

running_argument = "lrun --max-cpu-time {cpu_time} --max-real-time {real_time} --max-output {output_limit} " \
                   "--max-memory {memory} --network false --remount-dev true --reset-env true " \
                   "--syscalls '{blacklist}' {command} 3>&2"
user_output_file = "user.out"

def DoDiff(input_file, std_output_file, user_output_file, spj):
  if spj:
    return True
  else:
    return subprocess.call(['wcmp.bin', input_file, std_output_file, user_output_file]) == 0

def Judge(work_dir, data_dir, language_token, source_file, time_limit, memory_limit, output_limit, test_case, compile=False, spj=False):
  if int(memory_limit) < 1024:
    return "MLE"
  memory_limit = int(memory_limit) // 4 * 4
  work_dir = path.abspath(work_dir)
  if compile:
    try:
      compiler.Compile(language_token=language_token,
                       source_file=source_file,
                       work_dir=work_dir)
    except compiler.CompileError as e:
      return "CE\n" + e.message
  return Run(language_token=language_token,
             source_file=source_file,
             cpu_time=int(time_limit) / 1000.0,
             real_time=int(time_limit) / 1000.0 * 2,
             memory=int(memory_limit) * 1024,
             output_limit = int(output_limit) * 1024,
             test_case=test_case,
             data_dir=data_dir,
             work_dir=work_dir,
             spj=spj)

def Run(language_token, source_file, cpu_time, real_time, memory, output_limit, data_dir, test_case, work_dir, spj):
  work_dir = path.abspath(work_dir)
  data_dir = path.abspath(data_dir)
  input_file = path.abspath(data_dir + "/" + test_case + ".in")
  output_file = path.abspath(work_dir + "/" + user_output_file)
  running_command = util.judge_languages[language_token]["executive_command"] \
                        .format(source_file=source_file,
                                work_dir=work_dir,
                                input_file=input_file,
                                output_file=output_file)
  blacklist = util.judge_languages[language_token]["blacklist"]
  status, output = commands.getstatusoutput(running_argument.format(cpu_time=cpu_time,
                                                                    real_time=real_time,
                                                                    memory=memory,
                                                                    output_limit=output_limit,
                                                                    blacklist=blacklist,
                                                                    command=running_command))
  pivot = output.rfind("MEMORY   ")
  if pivot == -1:
    return "SE"
  if pivot:
    lrun_error = output[: pivot]
  else:
    lrun_error = None
  result = lrun.Parse(output[pivot:])
  if result["EXCEED"] != "none":
    if result["EXCEED"] == "MEMORY":
      return "MLE"
    elif result["EXCEED"] in ["CPU_TIME", "REAL_TIME"]:
      return "TLE"
    elif result["EXCEED"] == "OUTPUT":
      return "OLE"
    else:
      return "SE"
  if result["EXITCODE"] != "0" or result["SIGNALED"] != "0" \
     or result["TERMSIG"] != "0" or lrun_error or status != 0:
    return "RE"

  if DoDiff(path.join(data_dir, test_case + ".in"),
            path.join(data_dir,test_case + ".out"),
            path.join(work_dir, user_output_file), spj):
    return "AC\n" + str(result)
  else:
    return "WA"
