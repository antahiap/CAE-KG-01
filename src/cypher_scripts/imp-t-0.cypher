// imp_t0
match (p1:Part)-[r:BEHAVE_AS]-(e:Evt)-[:BEHAVE_AS]-(p2:Part)
where e.evt_id='t0_grad'
with e, p1, count(r) as rc
return distinct rc,e.evt_embd order by rc desc