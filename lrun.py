#
# Lrun executive result parser
#

lrun_record_default_length = 9


def Parse(record):
    result = {}
    for line in record.split("\n"):
        name = line[ : lrun_record_default_length].strip(" ")
        value = line[lrun_record_default_length : ]
        result[name] = value
    return result
