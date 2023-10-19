# Connect nodouts to parts
        
        - read nodout x,y,z id, time, name
        - clean the name
        - binout part information, no part information in the binout, it is just the node number, should read the model
                - why binout in meta return 3 curves
                - read binout in animator, in animator it is one curve, probably a bug in meta
        - [ ]  qdcae read femzip / use [lasso-python](https://github.com/lasso-gmbh/lasso-python)
                - dl femzip, [link](https://owncloud.sidact.com/owncloud/index.php/s/9e77cfeb083fdebd299d2014d0c66988?path=%2FFemzip-L)
                - uninstall qdcae
                - ask IT to compile the package with femzip
                - it seems can't install qd.cae with only femunzip
                - try unziping all with, `./femunzip_* -I <inputfile.fz> -O <outputfile>`
        - make keyfile
          - add #INCLUE_PATH to the master key file, key_assem.key
          - generate empty include for missing includes
          - If key is *INCLUDE_TRANSFORM with 0 transform replace it with *INCLUDE, (qd-cae doesn't work with INCLUDE_TRANSFORM )
          - all simulations have simillar includes => make one input key for all designs, pag.key
          - find the parts of the nodes 

        - generate Node in database
           - get node cordinate, from key file
           - evaluate max disp, from nodeout

- check if all the nodes are loaded
`match (s:Sim)	where not (s)-[]-()-[]-() return s.sim_name order by s.sim_name`

- [ ] Evaluate score/rank simulations
      - understand Graph possibilities
      - read graph algorithems
