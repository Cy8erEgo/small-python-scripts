#!/usr/bin/env python3

import subprocess 
import psutil
import os
import time


def create_child_processes():
    sites = ['google.com', 'yandex.ru', 'yahoo.com']

    for site in sites:
        proc = subprocess.Popen(['ping', site])

        print('[+] Created a child process with pid', proc.pid)

def kill_child_processes():
    cur_proc = psutil.Process(os.getpid())

    for child_proc in cur_proc.children(): 
        child_proc.kill()

        print('[-] Killed the process with pid', child_proc.pid)


if __name__ == '__main__':
    create_child_processes()

    print()

    time.sleep(15)

    print()

    kill_child_processes()


