import glob
import numpy as np
import KG_feed_OEM_data as KG
from qd.cae.beta import MetaCommunicator


if __name__ == '__main__':
    KG.neo4j_bolt('3687')

    OEM = 'Porsche'
    if OEM == 'Porsche':
        data_path = '/export/PAG_DATA/VORDERWAGEN/002_Daten_Kaan/ROB_VOWA_*'
        # keyIN = 'pag.key'
        dir_list = glob.glob(data_path)
        with open('src/box.npy', 'rb') as f:
            pids = np.load(f)
            rng = np.load(f)
            cog = np.load(f)

        for dir in dir_list:
            print(dir)
            sims = glob.glob(dir + '/Design*')
            ''' load or update all CAE simulations'''
            for s in sims:
                print(s)
                sim = KG.CaeSim()
                sim.dataP(s)
                # KG.make_box(sim)
                KG.update_part(sim, pids, rng, cog)
                # break
else:
    mc = MetaCommunicator(
        meta_path=(
                '/export/tools/BETA_CAE_Systems/'
                + 'meta_post_v19.1.6/meta_post64.sh'),
        ip_address='schauder', meta_listen_port=6007)
    print(mc.is_running())
