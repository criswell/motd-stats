MOTD STATS
==========

Sam's simple MOTD updater.

Puts very specific stuff in a MOTD subtable for sticking in `/etc/motd`.

Notes:
------

So, this is pretty specific, and not customizable at all (yet). The following
is relevant:

* It will probably only work with RPM-based systems. Currently using it on an
openSUSE system.
* It requires systemd and auth logs going to systemd's journal.
* It displays the running kernel info, as well as available kernel info. I
want this data so I can tell when I'm running a stale kernel and should reboot.
* It displays failed SSH login attempts. I get *a lot* of nasty baddies trying
to breach my machine. I want the top stats for the failed SSH attempts in
the last 24 hours along with IPs.
* It displays uptime data.

You probably want this in cron and piping the output to `/etc/motd`.

What's it look like?
--------------------

```
===========================================================================
  KERNEL INFO
===========================================================================
* Running Kernel: 4.13.12-1-default #1 SMP PREEMPT Wed Nov 8 11:21:09 UTC 2017 (9151c66)
* Available kernel(s):
                kernel-default-4.13.11-1.2.x86_64
                kernel-default-4.13.12-1.1.x86_64

===========================================================================
  FAILED SSH ATTEMPT STATS
===========================================================================
* User: root    Tries: 18405
        IP: XX.YY.83.22        Tries: 5254
        IP: XX.YYY.198.167      Tries: 4699
        IP: XX.YYY.83.20        Tries: 8236
* User: admin    Tries: 18405
        IP: XX.YYY.83.22        Tries: 5254
        IP: XX.YYY.198.167      Tries: 4699
        IP: XX.YYY.83.20        Tries: 8236

===========================================================================
  UPTIME : 18:15:01  up  21:02,  2 users,  load average: 0.19, 0.14, 0.05
===========================================================================
```
