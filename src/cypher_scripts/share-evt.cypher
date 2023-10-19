// share_evt
//share_meas
match (m:Des)-[:GROUPED_IN]-(p1:Part)-[r:BEHAVE_AS]-(e:Evt)-[:BEHAVE_AS]-(p2:Part)
where e.evt_id='tn_pct'
with m,p1,r,e, count(r) as rc
where rc=119

return m,p1,r,e