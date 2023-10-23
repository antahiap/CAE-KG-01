Model sample:
/home/ndv/data/TruckData
/home/apakiman/dataviewer_projects/Truck_example/Analysis_LB_001

 1. load models in it
    - how dataview plots parts
      it uses vtk output, possible to visualize this in paraview
      ./results_vtk_files
  
      - how to connect each vtk file to the cluster coordinate  
       ./results_embedings/embeddings.json, row number = ID
        - look into gitlab to find the visualization package
          - [install dataviewer code](https://gitlab.scai.fraunhofer.de/ndv/products/DataViewer/tree/master/cpp)
          - find ATK::atkvisualization  
        - mine dataviewer script
          - dl modelcompare lib
            - compare cmakelist of model compare and model compare extension
          - cpp code run
            - find the plot function
          - python
          -
        - install complete ATK lib   
          - add libraries in /usr/local/include/
        - 
        - 

      - where the cluster coordinate is stored
        - embedding coordinates in 
          ./results_embeddings/embeddings.json

      - which web based viewer is best to use (latest update, number of community member)
        - [ParaVieWeb](https://www.paraview.org/web/), JavaScript lib  
        - [vtk.js](https://kitware.github.io/vtk-js/), JavaScript  


      - try to plot vtk file with javascript package


 2. read the articles