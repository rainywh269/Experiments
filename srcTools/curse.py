#!/usr/bin/python

import curses
import time

def main(stdscr):
    global screen
    screen = stdscr.subwin(23,79,1,0)
    screen2= stdscr.subwin(1,79,0,0)
    screen.box()
    screen.refresh()
    c = screen2.getstr()
    screen.addstr("dfdf"+str(c),curses.A_BOLD)
    screen.addstr(,1,"dfdf"+str(c),curses.A_BOLD)
    screen.addstr(3,1,"dfdf"+str(c),curses.A_BOLD)
    screen.refresh()


if __name__ == '__main__':
    stdscr = curses.initscr()
    main(stdscr)
    time.sleep(5)
    curses.endwin()

