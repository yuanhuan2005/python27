#!/usr/bin/env python

n, m = 0, 1
while (m < 1000000):
    print n + m
    n, m = m, n + m
