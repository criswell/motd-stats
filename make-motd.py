#!/usr/bin/env python

import sys
import os
import json
import subprocess

def exec_cmd(cmd):
    #print(cmd)
    try:
        output = subprocess.check_output(cmd, shell=True)
        lines = output.split('\n')
        lines = [l.strip() for l in lines]
    except subprocess.CalledProcessError:
         return None

    if lines[-1] == '':
        lines.pop()
    return lines

kernel_rel = exec_cmd("uname -r")
kernel_ver = exec_cmd("uname -v")
uptime = exec_cmd("uptime")

failed_sshd = None
failed_sshd = json.loads(''.join(exec_cmd("journalctl -u sshd --since today -p err --no-pager -o json")))

print(failed_sshd)
