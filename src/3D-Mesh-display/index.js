import { OrbitControls } from "https://unpkg.com/three@0.122.0/examples/jsm/controls/OrbitControls.js";
let camera, controls, scene, renderer;

const toggleBtn = document.getElementById("toggle");
let visible = true;
//scene
scene = new THREE.Scene();

//camera
camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

//renderer
renderer = new THREE.WebGLRenderer();
controls = new OrbitControls(camera, renderer.domElement);

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(10, 10, 10);
const material = new THREE.MeshNormalMaterial({ wireframe: true });
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

const geometry2 = new THREE.SphereGeometry(10, 10, 10);
const material2 = new THREE.MeshNormalMaterial({ wireframe: true });
const sphere2 = new THREE.Mesh(geometry2, material2);
sphere2.position.x = 40;
scene.add(sphere2);

const geometry3 = new THREE.ConeGeometry(10, 20, 10);
const material3 = new THREE.MeshNormalMaterial({ wireframe: true });
const sphere3 = new THREE.Mesh(geometry3, material3);
sphere3.position.x = -40;
scene.add(sphere3);

camera.position.z = 70;

//controls = new THREE.OrbitControls(camera,renderer.domElement)
//controls.minDistance =1
//controls.maxDistance =1000
controls.update();

toggleBtn.addEventListener("click", () => {
  visible = !visible;
});

const animate = () => {
  requestAnimationFrame(animate);

  sphere.rotation.x += 0.02;
  sphere.rotation.y += 0.02;

  sphere2.rotation.x += 0.02;
  sphere2.rotation.y += 0.02;

  sphere3.rotation.x += 0.02;
  sphere3.rotation.y += 0.02;

  sphere.visible = sphere2.visible = sphere3.visible = visible;

  // required if controls.enableDamping or controls.autoRotate are set to true
  controls.update();

  renderer.render(scene, camera);
};

animate();
