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
