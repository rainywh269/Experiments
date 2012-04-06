#!/usr/bin/env python
# -*- coding: utf-8 -*-

import daemon
import time
import os.path as path

import fcntl
import os
import sys

class PidFile(object):
    """Context manager that locks a pid file.  Implemented as class
    not generator because daemon.py is calling .__exit__() with no parameters
    instead of the None, None, None specified by PEP-343."""
    # pylint: disable=R0903

    def __init__(self, path):
        self.path = path
        self.pidfile = None

    def __enter__(self):
        self.pidfile = open(self.path, "a+")
        try:
            fcntl.flock(self.pidfile.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            raise SystemExit("Already running according to " + self.path)
        self.pidfile.seek(0)
        self.pidfile.truncate()
        self.pidfile.write(str(os.getpid()))
        self.pidfile.flush()
        self.pidfile.seek(0)
        return self.pidfile

    def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
        try:
            self.pidfile.close()
        except IOError as err:
            # ok if file was just closed elsewhere
            if err.errno != 9:
                raise
        os.remove(self.path)

def main():
    print path.dirname(path.abspath(__file__))+'dfdf'
    with daemon.DaemonContext(stdout=sys.stdout, pidfile=PidFile(path.dirname(path.abspath(__file__))+'dfdf')):
        while True:
            time.sleep(10)
            print "100"

if __name__ == '__main__':
    main()
