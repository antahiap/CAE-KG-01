import meta
from meta import utils
import glob
import re
import os

pathdir = 'S:\\nobackup\\safety\\projects\\mma\\3_stv0\\front\\runs\\*fp3*'
lc_pose = 3
views = ['top', 'front', 'right']
states = '5/10/15/20/25/30/33'

print(pathdir)
dirs = (glob.glob(pathdir))
lc_dic = {}
for d in dirs:
    runName = d.split('\\')[-1]
    loadcase = runName.split('_')[lc_pose]

    modelPath = d + '\\' + runName + '.fz'
    if os.path.isfile(modelPath):
        print(runName)
        utils.MetaCommand('window delete "MetaPost"')
        utils.MetaCommand('window create "MetaPost"')
        utils.MetaCommand('window active "MetaPost"')
        utils.MetaCommand('model active all')

        utils.MetaCommand('options var add runName ' + runName)

        utils.MetaCommand('read geom Dyna3d ' + modelPath)
        utils.MetaCommand('read dis Dyna3d ' + modelPath + '  ' +  states +  '  Displacements')

        for v in views:
            print ('viesw:', v)
            utils.MetaCommand('options var add pos ' + v)
            utils.MetaCommand('options var add aniOn 1 ')
            utils.MetaCommand('read session pic_ani.ses')
            break

            for s in states.split('/'):
                print('states: ' + s)
                utils.MetaCommand('options var add pos ' + v)
                utils.MetaCommand('options var add st ' + s)
                utils.MetaCommand('options var add aniOn 0 ')
                utils.MetaCommand('read session pic_ani.ses')
                
                
