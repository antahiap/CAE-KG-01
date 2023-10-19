//N_part_for_each_sim
match (s:Sim)
with s
match (s)-[r:NRG_PART]-(p:Part)
return s.sim_abb, count(r) order by s.sim_abb