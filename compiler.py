#
# Compile module for specific language compiling.
#
from os import path
import commands
import util
import lrun


compile_argument = "lrun --max-real-time 10 {command} 3>&2"


class CompileError(Exception):
    """
    An error which indicates errors occur when compiling.
    """
    def __init__(self, message):
        super(CompileError, self).__init__(message)


def Compile(language_token, work_dir):
    """
    Compile specific language with provided source code.
    
    Args:
      language_token: the language token provided in util.py, as the key of judge language list
      source_file: the source code file name, with relative file name starts with currnet folder(.)
    """
    work_dir = path.abspath(work_dir)
    source_file = util.judge_languages[language_token]["source_file"]
    compile_command = util.judge_languages[language_token]["compile_command"] \
                          .format(source_file = source_file, work_dir = work_dir)
    status, output = commands.getstatusoutput(compile_argument.format(command = compile_command))

    pivot = output.rfind("MEMORY   ")
    if status or pivot == - 1 or "error" in output[ : pivot]:
        raise CompileError(output[ : pivot])

    result = lrun.Parse(output[pivot : ])

    if result["EXITCODE"] != "0" or result["TERMSIG"] != "0" \
       or result["SIGNALED"] != "0" or result["EXCEED"] != "none":
        raise CompileError("unknown reason")
    
    return True

