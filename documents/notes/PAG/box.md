#### Boxes
- get node cordinate range
- make box from the range
<img src="./img/box_sample.png" height="200px"/>

- [ ] make longitudinal boxes
        - dyna box options
        - use local coordinate sys option, sample `/home/apakiman/kg01/box_local.k`

<img src="./img/diagonal_box.png" height="200px"/>
<img src="./img/img3.png" height="200px"/>
        
        
- generate parts box as a key file
- wait with refining boxes until knowing more what kind of questions they are going to answer

- [ ] look into boxes in deformation
- [ ] save box info to neo4j, update_part


#### Merge Boxes
- comparison iteration
  - xz and xy plane cluster
<img src="./img/box_cluster_cog.png" height="200px"/>


compare B1 and B2, if < B1 is bigger: ref
- sort box based on cog
- remove nonshell parts, KG.make_box()
- C : cog_b1 - cog_b2
- if1 : C < rng_B1 : merge

<img src="./img/merge_boxes.png" height="200px"/>

-[ ] if2 : rng_B1 < C < (rng_B1 + rng_B2)/2 : ignore
-[ ] else: overlap pct: 
  - v1: MaxB1 - MinB1
  - v2: MaxB2 - MinB1
  - OVLP: v2/v1
  - if OVLP > thld:
        merge boxes min(minb1, minb2), max(maxb1, maxb2)

- make box_merge.k


<img src="./img/box_note_01.png" height="50px"/>
<img src="./img/box_note_02.png" height="50px"/>
