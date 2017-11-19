#!/usr/bin/env python

import sys
import os
import jsonlines
import subprocess

def exec_cmd(cmd):
    #print(cmd)
    try:
        output = subprocess.check_output(cmd, shell=True)
        if isinstance(output, bytes):
            output = output.decode('utf-8')
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

fssh_reader = jsonlines.Reader(exec_cmd("journalctl -u sshd --since today -p err --no-pager -o json"))

sshd_errors = {}

for obj in fssh_reader:
    if obj['MESSAGE'].startswith('error: PAM: Authentication failure for'):
        l = obj['MESSAGE'].split('error: PAM: Authentication failure for')
        p = l[-1].split('from')
        user = p[0].strip()
        ip = p[1].strip()
        if user in sshd_errors:
            sshd_errors[user].append(ip)
        else:
            ssdh_errors[user] = [ ip ]
