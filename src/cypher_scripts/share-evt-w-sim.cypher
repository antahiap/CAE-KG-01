// share_evt_w_sim
match (m:Des)-[:GROUPED_IN]-(p1:Part)-[r:BEHAVE_AS]-(e:Evt)-[:BEHAVE_AS]-(p2:Part)
where e.evt_id='tn_pct'
with m,p1,r,e, count(r) as rc
where rc=39
with p1,e,m
match (s:Sim)-[:NRG_PART]-(p1)
return s, p1,e,m