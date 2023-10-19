//count_share_evt
match (p1:Part)-[r:BEHAVE_AS]-(e:Evt)-[:BEHAVE_AS]-(p2:Part)
where e.evt_id='tn_pct'
with e, p1, count(r) as rc
where rc >4
return rc