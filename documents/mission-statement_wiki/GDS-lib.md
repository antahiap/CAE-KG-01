### Check Installation
- `call dbms.components() yield name, versions, edition unwind versions as version return name, version, edition` 
- `RETURN gds.version()`
----
### Graph Catalog

----
### Algorithms
- `gds.<algorithm>`, stable
- `ds.beta.<algorithm>`, candidate for production
- `gds.alpha.<algorithm>`, experimental


**input**: read from graph catalog or create it

**output**: `stream`, `stats`, `mutate`, `write`

**estimation**. `estimate`

[summarry](https://docs.google.com/spreadsheets/d/1wAzAyafQcCzyEqv53eM_-ywl7_ioc-y99wwvaoB_X54/edit?usp=sharing)
