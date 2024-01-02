#!/usr/bin/python3
for t in range(100):
    print('{:02d}'.format(t), end=(', ' if t < 99 else '\n'))
        
