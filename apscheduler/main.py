#!/usr/bin/env python
# -*- coding: utf-8 -*-
import daemon
from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(seconds=1)
def some_job():
    print "Decorated job"

#sched.configure(options_from_ini_file)
sched.configure(daemonic = False)

with daemon.DaemonContext():
    sched.start()
