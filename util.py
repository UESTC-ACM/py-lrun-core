#
# Utility settings for py-lrun-judge.
#
from os import path

c_language_blacklist = "!execve:k,flock:k,ptrace:k,sync:k,fdatasync:k,fsync:k,msync," + \
                      "sync_file_range:k,syncfs:k,unshare:k,setns:k,clone:k,query_module:k," + \
                      "sysinfo:k,syslog:k,sysfs:k"
java_language_blacklist = "!execve:k,flock:k,ptrace:k,sync:k,fdatasync:k,fsync:k,msync," + \
                         "sync_file_range:k,syncfs:k,unshare:k,setns:k," + \
                         "clone[a&268435456==268435456]:k,query_module:k,sysinfo:k," + \
                         "syslog:k,sysfs:k"

judge_languages = {
    "gnu-gcc": {
        "name": "GNU GCC",
        "extension": "c",
        "id": "1",
        "blacklist": c_language_blacklist,
        "compile_command": "gcc -static -w -O2 -DONLINE_JUDGE --std=c99 " + \
                           "{work_dir}/{source_file}.{extension} -lm -o " + \
                           "{work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin",
    },
    "gnu-g++": {
        "name": "GNU G++",
        "extension": "cc",
        "id": "2",
        "blacklist": c_language_blacklist,
        "compile_command": "g++ -static -w -O2 -DONLINE_JUDGE " + \
                           "{work_dir}/{source_file}.{extension} -o " + \
                           "{work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin",
    },
    "gnu-g++11": {
        "name": "GNU G++(std=g++0x)",
        "extension": "cc",
        "id": "3",
        "blacklist": c_language_blacklist,
        "compile_command": "g++ -static -w -O2 -DONLINE_JUDGE --std=gnu++0x " + \
                           "{work_dir}/{source_file}.{extension} -o {work_dir}/{source_file}.bin",
        "executive_command": "{work_dir}/{source_file}.bin",
    },
    "java": {
        "name": "Java8",
        "extension": "java",
        "id": "3",
        "blacklist": java_language_blacklist,
        "compile_command": "javac {work_dir}/{source_file}.{extension} -d {work_dir}",
        "executive_command": "java -cp {work_dir} -Djava.security.manager " + \
                             "-Djava.security.policy==%s {source_file}" % (path.abspath(".")),
    },
}
