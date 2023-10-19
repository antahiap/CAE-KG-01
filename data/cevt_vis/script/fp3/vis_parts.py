# PYTHON script
import glob
import re
import os

import pids

# runSet = [['3_stv0', ['fo5']], ['2_stcr', ['fp3', 'fo5', 'fod']]
#
# pathdir = '/share/nobackup/safety/projects/mma/{0}/front/runs/*{1}*'
# savePath = '/home/anahitapakiman/kg01/src/cevt_vis/Rep/{1}/vis'


def main():
    import meta
    from meta import utils

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
            utils.MetaCommand('options var add pidList ' + pidListStr)

            utils.MetaCommand('read geom Dyna3d ' + modelPath)

            for pid in pidList:
                print(pid)
                utils.MetaCommand('options var add pid ' + pid)
                utils.MetaCommand('read session vis_part.ses')
        break


def main2():
    import meta
    from meta import utils

    print(pathdir)
    d = glob.glob(pathdir)[0]
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
        utils.MetaCommand('options var add pidList ' + pidListStr)
        utils.MetaCommand('read geom Dyna3d ' + modelPath)

        for pid in pidList:
            print(pid)
            utils.MetaCommand('options var add pid ' + str(pid))
            utils.MetaCommand('read session vis_part.ses')

def list_missing_pics(dst, inPids):
    inPids.sort()
    avlPics = glob.glob(dst + '/*iso.png')
    avlPicPids = [int(x.split('/')[-1].split('_')[-2]) for x in avlPics]
    print(list(set(inPids) -set(avlPicPids)))
    for p in avlPicPids: #inPids:
        if str(p).startswith('55'):
            print(p)

lc_pose = 3
# states = '(1-2000-5)'
runSet = [['3_stv0', ['fp3', 'fo5', 'fod']], ['2_stcr', ['fp3', 'fo5', 'fod']]]

pathdir0 = '/share/nobackup/safety/projects/mma/{0}/front/runs/{1}'
savePath0 = '/home/anahitapakiman/kg01/src/cevt_vis/Rep/{0}/parts'

pidList = []
pidListStr = ''
for s in runSet:
    rls = s[0]

    rls0 = rls.split('_')[1]
    pidSimList = eval('pids.{}_pids'.format(rls0))
    savePath = savePath0.format(rls)

    pidListAll = []
    for sim in pidSimList:
        pidListAll += pidSimList.get(sim)
    pidListStr = ', '.join([str(x) for x in pidListAll])

    for sim in pidSimList:
        # print(sim)
        pathdir = pathdir0.format(rls, sim)
        pidList = pidSimList.get(sim)
        # main2()
    list_missing_pics(savePath, pidListAll)
    print(s[0], ': ', len(pidListAll))

    # 3_stv0 :  100   available: 100
    # 2_stcr :  130   available: 117


# pathdir0 = '/share/nobackup/safety/projects/mma/{0}/front/runs/*{1}*'
    # for lc in s[1]:
    #     pathdir = pathdir0.format(rls, lc)
    #     savePath = savePath0.format(rls)
    #
    #     if not os.path.isdir(savePath):
    #         os.makedirs(savePath)
    #
    #     rls0 = rls.split('_')[1]
    #     pidListStr += eval('pids.{}_{}'.format(rls0, lc))
    #     pidList += eval('pids.{}_{}'.format(rls0, lc)).split(',')
    #
    # pidList = list(set(pidList))
    # print(pidListStr)
    #
    # main()
