//remove label
MATCH (n:Evt)
REMOVE n:nrg:t0:tn
RETURN n.name, labels(n)