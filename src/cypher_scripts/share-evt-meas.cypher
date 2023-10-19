// share_evt_meas
//evt_meas
match (p:Part)-[r:BEHAVE_AS]-(e:Evt)-[:BEHAVE_AS]-(:Part)
where e.evt_id='tn_pct'
with e,p, count(r) as rc
where rc =39
with e,p
match (m:Des)-[:GROUPED_IN]-(p)
return e,p,m