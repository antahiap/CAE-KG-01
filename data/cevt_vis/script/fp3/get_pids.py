from neo4j import GraphDatabase
import numpy as np



def getPidList(rls, lc, r=0.1):
    cypherTxt = '''
            //meas_degree
            match (m:Meas)
            with m
            match (m)-[r:PART_MEAS]-(p:Part)
            where p.part_sim_name =~'.*{0}.*{1}.*'
            with count(r) as rc, m.meas_pid as pid
            return rc, pid order by rc desc
    '''.format(rls, lc)
    results = driver.session().run(cypherTxt.format())

    values = np.array(results.values())
    # rc []
    rc = values[:,0]
    pids = values[:,1]

    ids = np.where(rc > r*np.max(rc))
    pid_vis = pids[ids]
    print(', '.join([str(i) for i in pid_vis.tolist()] ))

def getPidSimList(rls):
    cypherMeas = '''
            //meas_degree
            match (m:Meas)
            with m
            match (m)-[r:PART_MEAS]-(p:Part)
            where p.part_sim_name =~'.*{0}.*'
            with count(r) as rc, m.meas_pid as pid
            return rc, pid order by rc desc
    '''.format(rls)
    results = driver.session().run(cypherMeas.format())

    values = np.array(results.values())
    # rc []
    rc = values[:,0]
    pids = values[:,1]

    sims = []
    for pid in pids:
        measSim = '''
            match (p:Part)
            where p.part_id = {0} and p.part_sim_name =~'.*{1}.*'
            return p.part_sim_name order by p.part_sim_name limit 1
            '''.format(pid, rls)
        results01 = driver.session().run(measSim.format())

        values = np.array(results01.values())
        sim = values[0,0]
        sims.append(sim)
    simsU = list(set(sims))
    simsU.sort()
    dic_sim = {}
    for su in simsU:
        dic_sim[su] = []
        # print(dic_sim.get(su))
        for i,si in enumerate(sims):
            if si == su:
                dic_sim[su].append(pids[i])
                # print(pids[i], si)
    print(dic_sim)
                # break




driver = GraphDatabase.driver(
    uri="bolt://localhost:7687", auth=("neo4j", "ivory123"))
runSet = [
            ['stv0', ['fp3', 'fo5', 'fod']],
            ['stcr', ['fp3', 'fo5', 'fod']]]
for s in runSet:
    rls = s[0]
    getPidSimList(rls)
    # break
#     for lc in s[1]:
#         print(rls, lc)
#         getPidList(rls, lc)
