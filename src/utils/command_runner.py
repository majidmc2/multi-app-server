import os


def popen(cmd):
    with os.popen(cmd) as s:
        result = s.read()
    return result
