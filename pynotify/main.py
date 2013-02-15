#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pyinotify
from os.path import join, dirname, abspath


class MyEventHandler(pyinotify.ProcessEvent):
    def process_default(self, event):
        f = event.pathname
        print f

class INotifyReloader():
    """Auto reloader employ inotify(7)
    """

    def __init__(self, watched_dirs):
        self._cwd = dirname(abspath(__file__))
        self.watched_dirs = watched_dirs

    def start(self):
        cwd = self._cwd
        wm = pyinotify.WatchManager()
        eh = MyEventHandler()

        notifier = pyinotify.ThreadedNotifier(wm, eh)
        notifier.daemon = True
        notifier.start()

        mask = pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_DELETE | \
                pyinotify.IN_MOVED_TO | pyinotify.IN_MOVED_FROM

        for watched_dir in self.watched_dirs:
            path = join(cwd, watched_dir)
            wm.add_watch(path, mask, rec=False, auto_add=True)

def main():
    watched_dirs = (
            #"movie/static",
            #"static",
            #"fm/static",
            "movie/templates"
            ,
            )
    static_refresher = INotifyReloader(watched_dirs)
    static_refresher.start()

if __name__ == '__main__':
    main()
