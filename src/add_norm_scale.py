import KG_feed_OEM_data as KG
import glob
import time

if __name__ == '__main__':
    KG.neo4j_bolt('3687')


    OEM = 'Porsche'
    if OEM == 'Porsche':
        data_path = '/export/PAG_DATA/VORDERWAGEN/002_Daten_Kaan/ROB_VOWA_505*'
        dir_list = glob.glob(data_path)
        count = 1

        for dir in dir_list:
            print(dir)
            i = 0
            sims = glob.glob(dir + '/Design*')
            ''' load or update all CAE simulations'''
            for s in sims:
                print(s)
                start = time.time()
                sim = KG.CaeSim()
                sim.dataP(s)
                print('inin')
                KG.populate_sim(sim)
                end = time.time()
                KG.trace_time(end-start, 'total')
                i += 1
                if i >= count:
                    break
            # break


    # sim = KG.Sim.nodes.get_or_none(sim_name='ROB_VOWA_505_Design0014')
    # print(sim)
