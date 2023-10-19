//limit_part
match (s:Sim)-[:NRG_PART]-(:Part)
call {
	with s
    match (s)-[:NRG_PART]-(p)
    return p
    limit 3
}
return p,s
