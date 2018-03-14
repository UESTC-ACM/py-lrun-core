#
# Utility settings for py-lrun-judge.
#
from os import path

c_language_blacklist = "!open:k,execve:k,flock:k,ptrace:k,sync:k,fdatasync:k,fsync:k,msync:k," + \
    "sync_file_range:k,syncfs:k,unshare:k,setns:k,clone:k,query_module:k,sysinfo:k,syslog:k,sysfs:k," + \
    "set_thread_area:k,mprotect:k,munmap:k,fork:k,vfork:k,getegid32:k,geteuid32:k,getuid32:k,getrlimit:k," + \
    "openat:k,set_robust_list:k,sigprocmask:k,rt_sigprocmask:k,ugetrlimit:k,writev:k,close:k"

java_language_blacklist = "!ugetrlimit,uname,rt_sigprocmask,sigprocmask," + \
                          "set_robust_list,openat," + \
                          "getrlimit,getuid32,getgid32,geteuid32,getegid32,set_tid_address," + \
                          "flock,ptrace,sync,fdatasync,fsync,msync," + \
                          "sync_file_range,syncfs:k,unshare,setns,clone[a&268435456==268435456]," + \
                          "query_module,sysinfo,syslog,sysfs,write,fork,vfork,munmap,set_thread_area"

python_language_blacklist = "!ugetrlimit,uname,rt_sigprocmask,sigprocmask," + \
                            "set_robust_list,openat," + \
                            "getrlimit,getuid32,getgid32,geteuid32,getegid32,set_tid_address," + \
                            "flock,ptrace,sync,fdatasync,fsync,msync," + \
                            "sync_file_range,syncfs:k,unshare,setns,clone[a&268435456==268435456]," + \
                            "query_module,sysinfo,syslog,sysfs,fork,vfork,munmap,set_thread_area,execve," + \
                            "writev"


judge_languages = {
    "gnu-gcc": {
        "name": "GNU GCC",
        "extension": "c",
        "id": "1",
        "blacklist": c_language_blacklist,
        "compile_command": "gcc -static -w -O2 -DONLINE_JUDGE --std=c99 -fmax-errors=15 " +
                           "{work_dir}/{source_file}.{extension} -lm -o " +
                           "{work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin < {input_file} > {output_file}",
    },
    "gnu-g++": {
        "name": "GNU G++",
        "extension": "cc",
        "id": "2",
        "blacklist": c_language_blacklist,
        "compile_command": "g++ -static -w -O2 -DONLINE_JUDGE -fmax-errors=15 " +
                           "{work_dir}/{source_file}.{extension} -o " +
                           "{work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin < {input_file} > {output_file}",
    },
    "gnu-g++11": {
        "name": "GNU G++(std=g++0x)",
        "extension": "cc",
        "id": "3",
        "blacklist": c_language_blacklist,
        "compile_command": "g++ -static -w -O2 -DONLINE_JUDGE --std=gnu++0x -fmax-errors=15 " +
                           "{work_dir}/{source_file}.{extension} -o {work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin < {input_file} > {output_file}",
    },
    "java": {
        "name": "Java8",
        "extension": "java",
        "id": "3",
        "blacklist": java_language_blacklist,
        "compile_command": "javac {work_dir}/{source_file}.{extension} -d {work_dir}",
        "executive_command": "bash -c \"java -cp {work_dir} -Djava.security.manager " +
                             "-Djava.security.policy==%s {source_file} \"" % (path.abspath(".") +
                                                                            " < {input_file} > {output_file}"),
    },
    "python3": {
        "name": "python3",
        "extension": "py",
        "id": "4",
        "blacklist": python_language_blacklist,
        "executive_command": "python3 {work_dir}/{source_file}.py < {input_file} > {output_file}",
    },
    "python2": {
        "name": "python2",
        "extension": "py",
        "id": "4",
        "blacklist": python_language_blacklist,
        "executive_command": "python2 {work_dir}/{source_file}.py < {input_file} > {output_file}",
    },
}
