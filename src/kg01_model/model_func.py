from neomodel import db


class MthdF:
    def cnct_part_fts(m, pid, simName, val):
        cypherTxt = '''
        MERGE (m:Mthd{{
            mthd_name: '{0}',
            mthd_cnfg_keys:{1},
            mthd_cnfg_vals:{2},
            mthd_keys:{3}
            }})
        with m
        match (p:Part)-[:NRG_PART]-(s:Sim)
        where p.part_id={4} and s.sim_name='{5}'
        merge (p)-[f:Fts]-(m)

        SET f.value ={6}
        '''.format(
            m['mthd_name'], m['mthd_cnfg_keys'],
            m['mthd_cnfg_vals'], m['mthd_keys'],
            pid, simName, val)

        # print(cypherTxt)
        db.cypher_query(cypherTxt)
