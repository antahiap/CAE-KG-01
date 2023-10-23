#### run c++ with web-server
framework (community size, last development, database)  
- scale framework, Angular, Django
- [cwf](https://www.cppwebframework.com/)  
- [cppcms](http://cppcms.com/wikipp/en/page/main )
-------------------------------------------------------------------------------------------------------
### 3D visualization
- JavaScript packages
  - [three.js](https://threejs.org/), [intro](http://davidscottlyons.com/threejs-intro/#slide-1)
    - [learning three.js](https://github.com/josdirksen/learning-threejs)
    - vtk.js
    - [xeolabs](http://xeolabs.com/)- [xeogl](http://xeogl.org/index.html)
  - html tag
    - use [model-viewer](https://developers.google.com/web/updates/2019/02/model-viewer)
-------------------------------------------------------------------------------------------------------
#### check 3D data format
possibility to load 5000 runs on cash with javascript/BufferGeometry)

##### Draco Format
(~/Projects/Truck_example/Analysis_LB_001) 
- [x] **OBJ or PLY files** to create .drc format (vtk to OBJ from dataviewer)
  - decode vtk file name, [md5](https://en.wikipedia.org/wiki/MD5)
  - convert dataviewer vtk output to OBJ/PLY, [meshio](https://pypi.org/project/meshio/),
             [conda instalation](https://anaconda.org/kayarre/meshio)
  - test draco file, use loader: javascript/example/webgl_loader_draco_advanced.html in [draco](https://github.com/google/draco)
> meshino python package, (~/Projects/python_lib/)decode_vtk_name.py, vtk_to_obj.py,  
- [x] run draco [example](https://github.com/google/draco/tree/master/javascript/example), use `python -m http.server`, for python 3

- [x] run ./draco-decode, do make after build
>`for i in *.obj; do echo $i; ./draco_encoder -i $i -o ../dir/"${i%.*}.drc";done`; 

- [x] combine output with draco sample case
  - run http server in, Truck_example/Analysis_LB_001/drc_javascript, [truck_part](http://localhost:8000/example/truck_webgl_loader_draco.html)
  - add rotation of the part, and toggle or engineering oriented package
  - find bunny positin relative to truck, read coordinates in ParaView, bunny at zero, part at x3800
  - set camera for the part, find correct function in tree.js
  - combine draco with xeogl - not beneficial, smaller community and not much available features
   

##### Cash Loading  
Be able to load time steps of the simulation as animation

- [x] Animation, [work extension](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/issues/40)
  - [Three.js animation strategy](https://threejs.org/docs/index.html#manual/en/introduction/Animation-system)
  - animation format that is required for Three.js [glTF](https://discoverthreejs.com/book/first-steps/load-models/), [more](https://www.khronos.org/gltf/)
  - [KHR_draco_mesh_compression](https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_draco_mesh_compression/README.md)
  - bufferGeometry from three.js for loading efficency, [more info](https://threejs.org/docs/#api/en/core/BufferGeometry)
  - [draco loader](https://threejs.org/docs/#examples/en/loaders/DRACOLoader)
  - [draco-animation](https://www.npmjs.com/package/draco-animation)  
- [x] overlay parts, [work extension](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/issues/40)
- [ ] point cloauds in three.js
  - [codeOpen](https://codepen.io/seanseansean/pen/EaBZEY), [edit cloud](https://stackoverflow.com/questions/49987104/editing-a-point-cloud-in-three-js), [physics](https://threejs.org/examples/?q=physics#webgl_physics_volume), [water](http://madebyevan.com/webgl-water/)
- [ ] Real-Time webgl visualization
  - [benchmarking](http://marcinignac.com/blog/fast-dynamic-geometry-in-webgl/)
-------------------------------------------------------------------------------------------------------
#### Outputting Number of Clusters
-------------------------------------------------------------------------------------------------------
#### Visualizing Cluster Representations

