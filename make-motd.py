#!/usr/bin/env python

import sys
import os
import jsonlines
import subprocess
from collections import Counter

# Possibly want these to come from  config... but for now, meh
MAX_SSH_LIST = 5
MAX_SSH_IPS = 3

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
            sshd_errors[user] = [ ip ]

class SSHD_Stat:
    def __init__(self, user, tries, counter):
        self.user = user
        self.tries = tries
        self.counter = counter
    def __repr__(self):
        return repr((self.user, self.tries, self.counter))

s = []
for k in sshd_errors.keys():
    s.append(SSHD_Stat(k, len(sshd_errors[k]), Counter(sshd_errors[k])))

sshd_stats = sorted(s, key=lambda stat : stat.tries)
print(sshd_stats)

motd = []

motd.append("FAILED SSH ATTEMPT STATS")
motd.append("========================")
i = 0
for s in sshd_stats:
    motd.append("* User: {0}\tTries: {1}".format(s.user, s.tries))
    k = 0
    for ip in s.counter:
        motd.append("\tIP: {0}\tTries: {1}".format(ip, s.counter[ip]))
        k = k + 1
        if k >= MAX_SSH_IPS:
            break
    i = i + 1
    if i >= MAX_SSH_LIST:
        break

for l in motd:
    print(l)
