#!/usr/bin/env python

import curses
import curses.wrapper

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
