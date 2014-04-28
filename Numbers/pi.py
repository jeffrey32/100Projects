#!/usr/bin/env python

import sys
from sympy.mpmath import mp

mp.dps = int(sys.argv[1])
if mp.dps > 100:
    print 'Too high'
else: print mp.pi

