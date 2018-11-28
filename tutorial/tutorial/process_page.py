# -*- coding:utf-8 -*-

# StdLib imports
import os
import time
import signal
import subprocess
from ctypes import cdll

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
WORKER_PATH = os.path.join(CURRENT_PATH, 'run_page.py')

POSITION_CMD = ['python3', WORKER_PATH]

INTERRUPT = 5
PROCESS_LIMIT = 1
PR_SET_PDEATHSIG = 1


class PrCtlError(Exception):
    pass


def on_parent_exit(signame):
    """
    Return a function to be run in a child process which will trigger
    SIGNAME to be sent when the parent process dies
    """
    signum = getattr(signal, signame)

    def set_parent_exit_signal():
        # http://linux.die.net/man/2/prctl
        result = cdll['libc.so.6'].prctl(PR_SET_PDEATHSIG, signum)
        if result != 0:
            raise PrCtlError('prctl failed with error code %s' % result)
    return set_parent_exit_signal


def schedule(cmd):
    all_process = []
    while 1:
        if len(all_process) < PROCESS_LIMIT:
            p = subprocess.Popen(
                cmd,
                preexec_fn=on_parent_exit('SIGTERM'),
            )
            all_process.append(p)
        for index, process in enumerate(all_process):
            if process.poll() is not None:
                all_process.pop(index)
        time.sleep(INTERRUPT)


if __name__ == "__main__":
    schedule(POSITION_CMD)
