import os
import networkx as nx
from neomodel import db
import matplotlib.pyplot as plt
from neomodel import config, Q
# import neomodel
from kg01_model.models import Part, Des, Behav, Sim  # , DesRel


class neomodelUpdate:

    def group_pid(rel='', lc='', dspln=''):
        print('Group PID')
        parts = Part.nodes.filter(
            Q(part_sim_name__contains=lc)
            & Q(part_sim_name__contains=rel)
            & Q(part_sim_name__contains=dspln)
        )

        for p in parts:
            pid = p.part_id
            # print(p.part_sim_name)
            # print(pid)

            print(p)
            des_curr = Des.nodes.get_or_none(des_pid=pid)
            if not des_curr:
                des_curr = Des(
                    des_type='pid',
                    des_pid=pid)
                des_curr.save()
            p.part_des.connect(des_curr)

    def nrg_behavior(fts_opt, method, type='nrg', lc='', rel='', dspln=''):
        print('NRG_behavior: ' + fts_opt)
        parts = Part.nodes.filter(
            Q(part_sim_name__contains=lc)
            & Q(part_sim_name__contains=rel)
            & Q(part_sim_name__contains=dspln)
        )

        for part in parts:
            fts = part.part_nrg(fts_opt)
            behav_old = Behav.nodes.get_or_none(
                behav_embd=fts,
                behav_method=method,
                behav_id=fts_opt)
            if behav_old:
                # print('behavior exist', behav_old.uid)
                behav_uid = behav_old.uid
                con = part.part_behav_con(behav_uid)
                if not con:
                    part.part_behav.connect(behav_old)
            else:
                # print('add behav for part', part.uid)
                behav = Behav(
                    behav_type=type,
                    behav_embd=fts,
                    behav_id=fts_opt,
                    behav_method=method)
                behav.save()
                part.part_behav.connect(behav)

    def connect_behav_des(lc='', rel='', dspln='', mType='pid'):
        print('connect behavior to design')
        sims = Sim.nodes.filter(
            Q(sim_name__contains=lc)
            & Q(sim_name__contains=rel)
            & Q(sim_name__contains=dspln)
        )
        for s in sims:
            # print(s.sim_name)
            deses = s.get_deses()
            for m in deses:
                des = Des.nodes.get_or_none(uid=m)
                behavs = des.get_behav()

                for e in behavs:
                    behav = Behav.nodes.get_or_none(uid=e)
                    # print(behav.uid)
                    des.des_behav.connect(behav)

    def connect_sim_behav(lc='', rel='', dspln=''):
        print('connect sim to behavior')
        sims = Sim.nodes.filter(
            Q(sim_name__contains=lc)
            & Q(sim_name__contains=rel)
            & Q(sim_name__contains=dspln)
        )
        for s in sims:
            # print(s.sim_name)
            behavs = s.get_behavs()
            for e in behavs:
                behav = Behav.nodes.get_or_none(uid=e)
                s.sim_behav.connect(behav)

    def connect_sim_des(lc='', rel='', dspln=''):
        print('connect sim to design')
        sims = Sim.nodes.filter(
            Q(sim_name__contains=lc)
            & Q(sim_name__contains=rel)
            & Q(sim_name__contains=dspln)
        )
        for s in sims:
            # print(s.sim_name)
            deses = s.get_deses()
            for m in deses:
                des = Des.nodes.get_or_none(uid=m)
                s.sim_des.connect(des)

    def connect_sim_des_weighted(ft='nrg_max', lc='', rel='', dspln=''):
        '''
            match (d:Des)-[r]-(s:Sim)-[]-(p:Part)
        where d.des_pid = p.part_id
        set r.weight=p.nrg_max
        //set r.weight=p.nrg_max/(p.tn_pct - p.ti_grad)
        //return max(r.weight), max(p.nrg_max ),
        return r.weight, p.nrg_max ,d.des_pid, p.part_id
        //return p
        '''
        print('connect sim to design')
        parts = Part.nodes.filter(
            Q(part_sim_name__contains=lc)
            & Q(part_sim_name__contains=rel)
            & Q(part_sim_name__contains=dspln)
        )
        for p in parts:
            pid = p.part_id
            w = p.part_nrg(ft)
            w = p.part_power()
            print(w)

            sim = Sim.nodes.get_or_none(uid=p.get_sim())
            des = Des.nodes.get_or_none(uid=p.get_des('pid'))
            sm = sim.sim_des.connect(des)
            sm.weight = w
            # print(sm)
            sm.save()

    def add_sym_des(pair_list, lc='', rel='', dspln=''):

        print('generate sym design')
        for pair in pair_list:
            pair.sort()
            parts = Part.nodes.filter(
                Q(part_id__in=pair)
            )
            pid = '_'.join([str(p) for p in pair])
            des_curr = Des.nodes.get_or_none(des_pid=pid)
            if not des_curr:
                des_curr = Des(
                    des_type='sym',
                    des_pid=pid)
                des_curr.save()

            for p in parts:
                p.part_des.connect(des_curr)

        print(type(parts))
        # print()

    def part_add_sim_name(lc='', rel='', dspln=''):
        print('add sim name to part')
        parts = Part.nodes.filter(
            Q(part_sim_name__contains=lc)
            & Q(part_sim_name__contains=rel)
            & Q(part_sim_name__contains=dspln)
        )
        for p in parts:
            sim_name = p.get_sim_name()
            # p(part_sim_name=sim_name)

            p.part_sim_name = sim_name[0]
            p.part_sim_abb = sim_name[1]
            p.save()

    def sim_add_info(OEM):
        print('update sim info')
        sims = Sim.nodes.all()
        for s in sims:
            if OEM == 'CEVT':
                if s.sim_path_post.endswith('/'):
                    s.sim_path_post = s.sim_path_post[:-1]
                rPath_split = s.sim_path_post.split('/')
                if len(rPath_split) == 1:
                    rPath_split = s.sim_path_post.split('\\')
                    s.sim_path_post = s.sim_path_post.replace('\\', '/')

                runName = s.sim_name
                release = rPath_split[-4].split('_')[1]
                dspln = rPath_split[-3]

                abb = runName.split('_')
                if len(abb) > 3:
                    loadcase = runName.split('_')[3]
                    abb = '_'.join([abb[2], abb[-1]])
                else:
                    loadcase = runName.split('_')[1]
                    abb = '_'.join([abb[1], abb[-1]])

                s.sim_abb = abb
                s.sim_lc = loadcase
                s.sim_rel = release
                s.sim_dspln = dspln
                # print(s)
                s.save()


class cyUpdate:

    def devTree(G, veh, cnfg, strc, model=False, mm=False, simDev=False):
        qi = cyTxt()
        pName = veh + '_{:04d}'

        if model:
            # Make Model nodes for the Sims
            print('Add Model nodes for each sim and connect to veh')
            for n in G.nodes():
                t1 = G.nodes[n]['t1']
                t2 = G.nodes[n]['t2']
                simName = pName.format(n)
                veh_abb = veh.split('_')[-1]
                db.cypher_query(
                    qi.m_cnct_sv.txt.format(
                        simName, veh, veh_abb, simName, t1, t2)
                )

        if mm:
            print('Connect Models based on dev tree')
            # make development tree connection
            for n in G.nodes():
                simName = pName.format(n)
                nb_list = [d for d in G.neighbors(n)]
                nb_list = [pName.format(x) for x in nb_list if x > n]
                # make Model nodes
                db.cypher_query(
                    qi.m_cnct_m.txt.format(simName, nb_list)
                )

        # make pltf and ubdy connected to veh
        print('conect veh to ubdy and pltf')
        db.cypher_query(
            qi.up_cnct_v.txt.format(
                veh,
                cnfg['ubdy_name'], cnfg['ubdy_spec'],
                cnfg['pltf_name'], cnfg['pltf_spec'])
        )

        # connect parts to Des with pid type
        print('conect parts to des pid type')
        db.cypher_query(
            qi.p_cnct_d.txt.format(veh + '.*'))

        # add weight to the NRG_PART
        print('Add absorption weight')
        db.cypher_query(
            qi.s_nrg_wgt_p.txt.format(veh + '.*', 'tn_pct'))

        # connect parts based on structural graph
        print('Add connection between the parts- STRUCTURAL GRAPH')
        for se in strc:
            db.cypher_query(
                qi.p_cnct_p.txt.format(
                    veh + '.*',
                    strc[se]['src'], strc[se]['trgt']
                ))

    def nrgWeight(w):
        qi = cyTxt()

        print('Add weight to NRG_PART edges with')
        print(w)
        db.cypher_query(
            qi.nrg_part.txt.format(w))

    def TL2PID(G, veh, model=False):
        print('restructure graph for TL2PID, learning from DOE')
        qi = cyTxt()

        if model:
            # Make Model nodes for the Sims
            print('Add Model nodes for each sim')
            pNameM = 'des_{:04d}'
            pNameS = veh + '_{:04d}'
            for n in G.nodes():
                simName = pNameS.format(n)
                mdlName = pNameM.format(n)
                veh_abb = veh.split('_')[-1]
                db.cypher_query(
                    qi.m_cnct_sv.txt.format(simName, veh, veh_abb, mdlName)
                )

            # make development tree connection, same model for all veh
            for n in G.nodes():
                mdlName = pNameM.format(n)
                nb_list = [d for d in G.neighbors(n)]
                nb_list = [pNameM.format(x) for x in nb_list if x > n]
                # make Model nodes
                db.cypher_query(
                    qi.m_cnct_m.txt.format(mdlName, nb_list)
                )


class cyTxt:

    class m_cnct_m:
        txt = '''
            // cnct_model_model
            MATCH (m:Model), (mn:Model)
            WHERE m.model_name='{}' AND mn.model_name IN {}
            MERGE (mn)-[r:MODEL_REF]->(m)
            RETURN m, mn
            '''

    class m_cnct_sv:
        txt = '''
            // create_model_cnct_sim_veh
            MERGE (v:Veh{{ veh_name: '{1}', veh_abb:'{2}'}})
            WITH v
            MATCH (s:Sim)
            WHERE s.sim_name='{0}'
            WITH s,v
            MERGE (m:Model{{ 
                model_name: '{3}', model_abb: s.sim_abb}})
            SET m.t1={4}, m.t2={5}
            MERGE (s)-[rs:SIM_MODEL]->(m)
            MERGE (m)-[rv:MODEL_VEH]-(v)
            RETURN s, m, v
        '''

    class up_cnct_v:
        txt = '''
            // create_ubdy_pltf_cnct_v
            MERGE (v:Veh{{ veh_name: '{0}'}})
            MERGE (u:Ubdy{{ ubdy_name: '{1}', ubdy_spec:'{2}'}})
            MERGE (p:Pltf{{ pltf_name: '{3}', pltf_spec:'{4}'}})
            WITH v,u,p
            MERGE (v)-[r1:VEH_PLTF]-(p)
            MERGE (v)-[r2:VEH_UBDY]-(u)
            RETURN v, u, p
        '''

    class p_cnct_d:
        txt = '''
        //create_des_cnct_p
        MATCH (s:Sim) WHERE s.sim_name=~'{0}'
        with s
        MATCH (s)-[:NRG_PART]-(p:Part)
            with p
            MERGE (d:Des{{des_type: 'pid', des_pid:p.part_id}})
            MERGE (p)-[r:PART_DES]-(d)
        return p, d
        '''

    class s_nrg_wgt_p:
        txt = '''
        //concatinate_nrg_fts_to_sim_weight_part
        MATCH (s:Sim) WHERE s.sim_name=~'{0}'
        with s
        MATCH (s)-[r:NRG_PART]-(p:Part)
        SET r.weight=p.{1}
        '''

    class p_cnct_p:
        txt = '''
        // part_cnct_part_structural
        MATCH (p1:Part)-[:NRG_PART]-(s:Sim) 
        MATCH (p2:Part)-[:NRG_PART]-(s)
        WHERE s.sim_name=~'{0}' AND
              p1.part_id={1} AND p2.part_id={2}
        MERGE (p1)-[r:CNCT_TO]->(p2)
        
        '''

    class nrg_part:
        # match (s:Sim)-[r:NRG_PART]-(p:Part)

        # set r.weight={0}
        # return r
        txt0 = '''
        // add weight to NRG_PART
        match (s:Sim)-[:NRG_PART]-(p:Part)
        //where s.sim_abb=~'000.*'
        call{
            with s,p
            match  m = (s)-[r:SIM_DES]-(d:Des)-[dp:PART_DES]-(p)
            set r.weight = p.nrg_max/(p.tn_pct - p.ti_grad)
            return r.weight as rw
        }
        
        return p.nrg_max, p.tn_pct, p.ti_grad, rw, p.part_sim_name, s.sim_abb 
        '''
        txt = '''
        // add weight to NRG_PART
        match (s:Sim)-[:NRG_PART]-(p:Part)
        where s.sim_abb=~'.*'
        call{
            with s,p
            match  m = (s)-[r:SIM_DES]-(d:Des)-[dp:PART_DES]-(p)
            set r.w_e_value = [p.nrg_max, p.nrg_max/(p.tn_pct - p.ti_grad)]
            set r.w_e_key = ['IE', 'P_e']
            return r.w_e_value as rw, r.w_e_key as rk
        }
        
        return p.nrg_max, p.tn_pct, p.ti_grad, rw,rk,  p.part_sim_name, s.sim_abb 
        '''

        txt_grp = '''
        // add weight to GRP_FTS
        match (s:Sim)-[r:GRP_FTS]-(g:Grp)
        where s.sim_abb=~'.*'
        call{
            with s,g, r
            set r.w_e_value = [r.grp_e_value[0], r.grp_e_value[0]/(r.grp_e_value[1] - r.grp_e_value[2])]
            set r.w_e_key = ['IE', 'P_e']
            return r.w_e_value as rw, r.w_e_key as rk
        }
        
        return r.grp_e_value, rw,rk , s.sim_abb 
        '''


if __name__ == '__main__':
    # OEM = 'Porsche'
    OEM = 'CEVT'
    OEM = 'YARIS'
    upm = neomodelUpdate()

    feat_list = [
        "nrg_max",  # 0

        "ti_grad",  # 1
        "ti_ll",  # 2

        "tn_pct",  # 3
        "tn_max"]  # 4
# ------------------------------------------------------------
    fts_opt = [feat_list[i] for i in [0, 1, 3]]
    # fts_opt = [feat_list[i] for i in [0, 3]]
    fts_id = ['IE', 'ti', 'tn']
    method = 'IE_ti_tn'

    print('-------------------------------')
    print('           ' + OEM + '         ')
    print('-------------------------------')
    print('features :', fts_id)
    print('method   :', method)
    print('-------------------------------')

    if OEM == 'Porsche':
        config.DATABASE_URL = os.environ.get(
            'NEO4J_BOLT_URL', 'bolt://neo4j:ivory123@localhost:3687')
        upm.group_pid()
        for f in fts_opt:
            upm.nrg_behavior(f, method)
    elif OEM == 'CEVT':
        config.DATABASE_URL = os.environ.get(
            'NEO4J_BOLT_URL', 'bolt://neo4j:ivory123@localhost:7687')

        # for f in fts_opt:
        #     nrg_behavior(f, method)

        # group_pid()
        # part_add_sim_name()
        # sim_add_info(OEM)
        # connect_behav_des()
        # connect_sim_behav()
        # connect_sim_des()
        upm.sim_add_info(OEM)

        cText = '''
        MATCH (e:Behav)
        RETURN
        CASE e.behav_id
        WHEN 'nrg_max'  THEN set e :nrg
        WHEN 'ti_grad' THEN set e :ti
        WHEN 'tn_pct' THEN set e :tn
        END AS result

        MATCH (e:Behav) where e.behav_id='nrg_max' set e :nrg return e
        MATCH (e:Behav) where e.behav_id='ti_grad' set e :ti return e
        MATCH (e:Behav) where e.behav_id='tn_pct' set e :tn return e
        '''
    elif OEM == 'YARIS':
        config.DATABASE_URL = os.environ.get(
            'NEO4J_BOLT_URL', 'bolt://neo4j:ivory123@localhost:7687')
        upm.group_pid()
        upm.connect_sim_des_weighted('nrg_max')
        # upm.connect_sim_des()
        upm.connect_behav_des()
        upm.connect_sim_behav()
