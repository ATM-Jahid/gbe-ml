#!/usr/bin/env python3

import os

comps = [0.2]
#comps = [0, 0.2, 0.4, 0.7]
tilts = [100, 190, 150, 140, 130, 170, 370, 120, 350, 230, 340]

perm = [[x, y] for x in comps for y in tilts]

for itr in perm:
    os.system(f'$HOME/builds/UMoly/scripts/replicator.py -i grain \
            -x 50 -y 200 -z 15 -a {itr[1]} -M {itr[0]} \
            -o umo_c{itr[0]}_a{itr[1]}_')
    os.system(f'$HOME/builds/lammps/build/lmp -i in.umo_c{itr[0]}_a{itr[1]}_1')