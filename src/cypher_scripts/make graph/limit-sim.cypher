//limit sim
match (s:Sim)
with s limit 10
match (s)-[:NRG_PART]-(p:Part)
return *