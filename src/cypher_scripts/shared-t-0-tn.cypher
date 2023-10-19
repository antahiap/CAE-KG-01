// shared_t0_tn
match (t2:tn)-[:BEHAVE_AS]-(m:Part)-[:BEHAVE_AS]-(t1:t0)
with m, t2, t1
match (t2)-[:BEHAVE_AS]-(n:Part)-[:BEHAVE_AS]-(t1)
with n, m, t1, t2
match (t2)-[r:BEHAVE_AS]-(p:Part)-[:BEHAVE_AS]-(t1)
with p, count(r) as rc, n, t1, t2
where rc = 50
with  n,p,t1,t2
match (M1:Des)-[:GROUPED_IN]-(p) 
with  n,p,t1,t2, M1
match (M2:Des)-[:GROUPED_IN]-(n)
return M1, M2, t1, t2, n, p
 
