#!/bin/bash

# usage : Deform_mode_input_3 <secs> <#nodes>

export perhost=4

PREF=log.$$
SCRIPT=${PREF}

narg=$#
args=($@)

if [ $narg -gt 0 ]; then
   x=${args[$(($narg-1))]}
   if [ $x -gt 0 ]; then
      nnod=$x
   fi
else
   nnod=1
fi

if [ $narg -gt 1 ]; then
   wtim=$1
else
   wtim=12200
fi

hr=$(($wtim/3600))
min=$(($wtim/60-60*$hr))
sec=$(($wtim-3600*$hr-60*$min))

echo "hr/min/sec" $hr $min $sec

export runnod=$(($perhost*$nnod))
export MYDIR=${PWD}
export JDIR=${MYDIR}
export HOSTFILE=${MYDIR}/hostfile

echo perhost $perhost
echo jdir $JDIR
echo nnod $nnod
echo runnod $runnod
echo hostfile $HOSTFILE

cd ${MYDIR}

# Lsdyna input deck and memory requirement 
export INPUTFILE=`basename *.key`
export memory=2G
export memory2=2G

# below, set the correct LSDYNA_EXECUTABLE
export driver=/home/apakiman/DYNA_R10/ls-dyna_hyb_s_r10_0_118302_x64_redhat54_ifort160_avx2_intelmpi-413

cat << EOF > ${JDIR}/${SCRIPT}
#!/bin/csh -x
cd ${MYDIR}
setenv LSTC_LICENSE network
setenv LSTC_LICENSE_SERVER schauder.scai.fraunhofer.de
# statements below probably not necessary for LSDYNA accessed via module load:
# module load intel/2018.02
# setenv KMP_AFFINITY compact
# module load intel
mpirun ${driver} I=${INPUTFILE} NCPU=1 MEMORY=${memory}  MEMORY2=${memory2}
EOF

# other partitions are possible
sbatch -N ${nnod}-${nnod} --partition=loewenburg-all --ntasks=${runnod} --exclusive -t ${hr}:${min}:${sec} ${JDIR}/${SCRIPT}

# as an alternative use reservation my_reservation, if active:
# sbatch -N ${nnod}-${nnod} --reservation=my_reservation --ntasks=${runnod} --exclusive -t ${hr}:${min}:${sec} ${JDIR}/${SCRIPT}
