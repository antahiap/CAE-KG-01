<dl>
<dt>NDV</dt>
<dd>/home/compeng</dd>


<dt>Atom</dt>
<dd>shortcuts	 	ctrl+shift+p</dd>
<dd>setting		ctrl+,</dd>
<dd>comment		ctrl+/</dd>
<dd>switch tab		ctrl+,</dd>
<dd>install package-sync> generate  ~/.atom/[packages.cson](/atom-package-list)> run Sync (ctrl+shift+P) </dd>
<dd> python [setup](https://hackernoon.com/setting-up-atom-as-a-python-ide-a-how-to-guide-o6dd37ff) </dd>
<dd> apm install linter-ui-default@2.4.1 </dd>

<dt>virenv conda</dt>
  <dd>conda activate ./env</dd>
  <dd>conda deactivate</dd>
  <dd>conda create --prefix ./envs python=3.4 --no-default-packages</dd>
  <dd>conda env create -f <path>/Web_App/environment.yml</dd>

<dt>python</dt>
  <dd>pipreqs /path/to/project</dd>
  <dd>conda install pip</dd>
  <dd>conda create -n py36 python=3.6 (anaconda)</dd>
  <dd>conda install --yes --file requirements.txt </dd>

  <dd>pip install -r requirements.txt</dd>

  <dd>**qd-cae**
      <dd>dyson:~/usr/src</dd>

</dd>

<dt>GIT</dt>
  <dd>git submodule update --init --recursive</dd>
  <dd>git clone </dd>
  <dd>https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts

* git init .
* git add merge.txt
* git commit -am "we are commiting the initial content"
* git checkout -b new_branch_to_merge_later
* git checkout master
* git merge new_branch_to_merge_later
* git status
* git stash
* cat merge.txt
* git grep "regexp" $(git rev-list --all)
* git diff rev1:file rev2:file
* git checkout rev1
* git reflog
* git reset --soft HEAD~1
transfer work structure, 
 - transfer reporting from issue to readme.md
 - have the codes on gitLAB
git clone </dd>


  <dt>Submodule<\dt>
  <dd>

* Make sure a new git repo already exist that will hold the content of the new submodule, for example, we'll be using "git@github.com:/newemptyrepo"
* Navigate to the directory you're modulizing:`cd myproject/submodule-dir`
* Remove the to-be submodule from the parent's index:`git rm -r --cached .`
* Init a new git repo inside the to-be submodule: `git init`
* Set up the origin for the to-be submodule and make your first commit:
```
     git remote add origin git@github.com:/newemptyrepo
     git add . && git commit && git push --set-upstream origin master
```
* Now you must navigate to the parent repo's top-level path:`cd .. && cd `git rev-parse --show-toplevel`
* Finally, add the submodule as you would normally: `git submodule add git@github.com:/newemptyrepo ./myproject/submodule-dir`
* Now commit & push the changes the above command makes and you're all set up!
* git submodule foreach git push origin master
</dd>

<dt>Shell</dt>

  <dd>ssh no password [link](https://www.thegeekdiary.com/how-to-run-scp-without-password-prompt-interruption-in-linux/)
  <dd> for i in ./*; do if [ ! -f $i/weld.json ]; then echo $i; fi; done </dd>
  <dd>for i in *; do if [ ! -f $i/weld.json ]; then mv  $i "no_data_${i}" ; fi; done</dd>
  <dd>for i in *; do p=`pdfinfo $i/report.pdf | grep Pages| grep 5`; if [ "$p" ]; then echo $i; echo $p ;fi ;done</dd>
  <dd>for i in ROB_VOWA_*/Design*/; do cd $i; if [ $(ls| wc -l) -lt 34 ]; then pwd; ls;fi; cd ../..;  done</dd>
  <dd> yum search </dd>
  <dd>new tab		ctrl+shift+T</dd>
  <dd>switch tab 	alt+1, alt+2</dd>
  <dd>find . &gt; files_and_folders 2&gt; &gt;(grep -v 'Permission denied' &gt;&amp;2)</dd>
  <dd>printenv</dd>
  <dd>find listed extension, find . -type f |perl -ne 'print $1 if m/\.([^.\/]+)$/' | sort -u</dd>
  <dd>java -jar azk.jar</dd>
  <dd>backkup: module load Java/1.8.0_141> dsmj, look into backup restor, /export/apakiman</dd>
  <dd>TRASH: `/home/apakiman/.local/share/Trash/files`</dd>
  <dd>
* if dyson is again slow, please check via htop and when gnome-keyring-daemon is eating 2 cpu cores again, kill it using

```
killall -9 gnome-keyring-daemon
```
</dd>


<dt>Paraview</dt>
  <dd>filter search	 ctrl+space</dd>

<dt>CPP</dt>
  <dd>source scl_source enable devtoolset-8</dd>
  <dd>gcc </dd>

<dt>NEO4J</dt>
  <dd>[ubuntu installation](https://neo4j.com/docs/operations-manual/current/installation/linux/tarball/)
  </dd>
  <dd>call db.schema.visualization()</dd>

<dt>Ivory</dt>
 <dd>source scl_source enable devtoolset-8</dd>

<dt>leo1</dt>
 <dd>sshfs leo1:/home/apakiman ~/leo1/</dd>
 <dd>ssh -X leo1</dd>
 <dd>module load Anaconda3/5.1.0</dd>
 <dd>source activate idp</dd>
 <dd>conda create --clone idp --prefix=~/myconda</dd>
 <dd> [gpu submition](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/-/tree/master/crashTest_CNN#leo1)</dd>
<dd> [GNN](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/-/issues/166#leo-setup)</dd>
<dd>[tensorflow 1.15](https://fmorenovr.medium.com/install-conda-and-set-up-a-tensorflow-1-15-cuda-10-0-environment-on-ubuntu-windows-2a18097e6a98)</dd>


<dt>vnc</dt>
 <dd>run putty > vncserver> check if it runs: ps aux | grep vnc > read errors in,  vim ~/.vnc/dyson\:1.log</dd>

<dt>LS-DYNA</dt>
 <dd> intel version: intel/2018.02, load module intel/2018.02</dd>
 <dd> submission script :[dyna.sh](uploads/4af0a15a88b2fce99ea1cd54c6e9e006/dyna.sh), should be on the `master.key` directory </dd>
 <dd>module load intel/2018.02
module load  ls-dyna/12.0.0
module load ansys/ansys-2022R1-ac</dd>
 <dd> squeue </dd>
 <dd>[IT wiki](https://it-wiki.scai.fraunhofer.de/index.php?title=SCAI_Loewenburg_Cluster)</dd>
 <dd>[LSDYNA Manual](https://www.dynasupport.com/manuals/ls-dyna-manuals/ls-dyna-manual-r10.0-vol-i)</dd>
 <dd> Project links: [HI workflow](https://gitlab.scai.fraunhofer.de/anahita.pakiman/mission-statement/-/issues/48), [YARIS Front](https://gitlab.scai.fraunhofer.de/anahita.pakiman/kg01/-/blob/master/documents/YARIS/model_setup.md)



<dt>Desparo</dt>
<dd>/home/ndv/tools/DesParO-version3/DesParO_3_0_centos8_lin64/batch/newmodel_batch</dd>
<dd>/home/ndv/tools/DesParO-version2/DesParO-release-24-lin64 > doc>index.html </dd>
<dd>6.1.2</dd>
<dd>Kdetr =1 /2</dd>
<dd>cleanPar, start with 0 and then 1 for cleanParThresh</dd>
<dd>cleanParThresh, 0.1</dd>
<dd>./newmodel_batch 2.0 3 1 310 1 0.01 0.1 0.01 0 10000 0 0 0 0 /home/ndv/stud/data/YARIS/full_front/TL2PID/DesParO_0102 /home/ndv/stud/data/YARIS/full_front/TL2PID/DesParO_0102/input_file.txt semicolon</dd>
<dd>7.2</dd>
<dd>/home/ndv/tools/DesParO-version3/PreRelease-DesParO_3_0-lin64/lin64/batch</dd>
<dd>./evaluate 1 /home/ndv/stud/data/YARIS/full_front/TL2PID/DesParO_0102/parameter_file.txt > /home/ndv/stud/data/YARIS/full_front/TL2PID/DesParO_0102/criteria_file.txt</dd>


<dt>ansa/meta</dt>
 <dd>check licence: `/home/compeng/beta_cae/BETA_CAE_Systems/beta_lm_tools_v6.4/linux_64/beta_lm_stat -a -h schauder`</dd>
<dd>source /home/compeng/config/env_beta_cae20.0.sh</dd>
<dd>meta_post64.sh</dd>

</dl>
