//meas_degree
match (m:Des)
with m
match (m)-[r:PART_MEAS]-(:Part)
with count(r) as rc, m
return rc, m.meas_pid order by rc desc
