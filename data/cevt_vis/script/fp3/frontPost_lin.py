# PYTHON script
import meta
from meta import utils
import glob
import re
import os

import pids

# runSet = [['3_stv0', ['fo5']], ['2_stcr', ['fp3', 'fo5', 'fod']]
#
# pathdir = '/share/nobackup/safety/projects/mma/{0}/front/runs/*{1}*'
# savePath = '/home/anahitapakiman/kg01/src/cevt_vis/Rep/{1}/vis'


def main():
    print(pathdir)
    dirs = (glob.glob(pathdir))
    lc_dic = {}
    for d in dirs:
        runName = d.split('/')[-1]
        loadcase = runName.split('_')[lc_pose]

        modelPath = d + '/' + runName + '.fz'
        if os.path.isfile(modelPath):
            print(runName)
            utils.MetaCommand('window delete "MetaPost"')
            utils.MetaCommand('window create "MetaPost"')
            utils.MetaCommand('window active "MetaPost"')
            utils.MetaCommand('model active all')

            utils.MetaCommand('options var add runName ' + runName)
            utils.MetaCommand('options var add savePath ' + savePath)
            utils.MetaCommand('options var add pidList ' + pidList)

            utils.MetaCommand('read geom Dyna3d ' + modelPath)
            utils.MetaCommand('read dis Dyna3d ' + modelPath + '  ' +  states +
            '  Displacements')

            for v in views:
                print ('viesw:', v)
                utils.MetaCommand('options var add pos ' + v)
                utils.MetaCommand('options var add aniOn 1 ')
                utils.MetaCommand('read session pic_ani.ses')

                nState = len(states.split('/'))
                for s in range(0, nState+1):
                    print('states: ' + str(s))
                    utils.MetaCommand('options var add pos ' + v)
                    utils.MetaCommand('options var add st ' + str(s))
                    utils.MetaCommand('options var add aniOn 0 ')
                    utils.MetaCommand('read session pic_ani.ses')



lc_pose = 3
views = ['top', 'front', 'right', 'btm']
states = '5/10/15/20/25/30/33'
states = '5/10/15/20/25/30/35/40/45/50/55/57/33'
# states = '(1-2000-5)'
runSet = [['3_stv0', ['fp3', 'fo5', 'fod']], ['2_stcr', ['fp3', 'fo5', 'fod']]]
runSet = [['3_stv0', ['fo5']], ['2_stcr', ['fo5' ]]]

pathdir0 = '/share/nobackup/safety/projects/mma/{0}/front/runs/*{1}*'
savePath0 = '/home/anahitapakiman/kg01/src/cevt_vis/Rep/{0}/{1}/vis'

print(runSet)
for s in runSet:
    rls = s[0]
    for lc in s[1]:
        pathdir = pathdir0.format(rls, lc)
        savePath = savePath0.format(rls, lc)

        if not os.path.isdir(savePath):
            os.makedirs(savePath)

        rls0 = rls.split('_')[1]
        pidList = eval('pids.{}_{}'.format(rls0, lc))

        main()
