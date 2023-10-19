//embd_nrg_graph
match (s:Sim)
with s limit 2
match (s)-[:NRG_PART]-(p:Part)-[:PART_EVT]-(e:Evt)
with s,e,p
match (p)-[:PART_MEAS]-(m:Meas)
return s,e,p,m