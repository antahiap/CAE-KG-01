import os
import pids



runSet = [['3_stv0', ['fo5']], ['2_stcr', ['fp3', 'fo5', 'fod']]]

print(runSet)
for s in runSet:
    rls = s[0]
    for lc in s[1]:
        rls0 = rls.split('_')[1]
        print(eval('pids.{}_{}'.format(rls0, lc) ))
