// shared_t0_tn_part_id
match (t2:tn)-[:BEHAVE_AS]-(m:Part)-[:BEHAVE_AS]-(t1:t0)
with m, t2, t1
match (t2)-[:BEHAVE_AS]-(n:Part)-[:BEHAVE_AS]-(t1)
with n, m, t1, t2
match (t2)-[r:BEHAVE_AS]-(p:Part)-[:BEHAVE_AS]-(t1)
with p, count(r) as rc, n, t1, t2
where rc = 50
with collect(n) as p1, collect(p) as p2
unwind (p1+p2) as N
return distinct id(N) order by id(N)

 
