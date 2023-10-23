a branch of [dataviewer issue](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/issues/32)
 - run three.js example, use `python -m http.server`, for python 3
 - in (~/Projects/Truck_example/Analysis_LB_001/drc_javascript)

------------------------------------------------------------------------------------------------------------
### pymesh
- installation, python36 (`conda activate py36`)
- `conda install -c conda-forge pymesh2`
- import pymesh
------------------------------------------------------------------------------------------------------------
### gltf
#### codes
written in python, (python_lib/gltf_sample.py)
- [gltf viewer](https://gltf-viewer.donmccurdy.com/), choose .glTF and .bin
- [three.js glft viewer](http://localhost:8000/example/webgl_loader_gltf.html)

#### understanding
-  camera understanding [link](https://observablehq.com/@grantcuster/understanding-scale-and-the-three-js-perspective-camera)
- [properties](https://www.khronos.org/files/gltf20-reference-guide.pdf), [link2](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_009_Meshes.md)
- [mesh-node](https://computergraphics.stackexchange.com/questions/7519/how-mesh-geometry-data-vertex-coordinates-stored-in-gltf)
- [toturial](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/README.md)

#### python mesh
 - [trimesh](https://trimsh.org/index.html), [examples](https://trimsh.org/examples.html)
 - [meshrender](https://berkeleyautomation.github.io/meshrender/index.html)
 - [gltflib](https://pypi.org/project/gltflib/)

#### animation
- needs to define skeleton to be able to define a mesh or split each element to separate scene.

----------------------------------------------------------------------------------
- add vtk mesh time 0 to gltf mesh
- read 5 time step to generate animation
![image](/uploads/0ce5883f2a53f120b2d77050af5dfb41/image.png)