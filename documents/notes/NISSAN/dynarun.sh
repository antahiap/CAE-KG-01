#!/bin/bash

# usage : Deform_mode_input_3 <secs> <#nodes>

#module load ansys/ansys-2022R1-ac

#module load ls-dyna/12.0.0

#export LSTC_FILE=network
export LSTC_LICENSE=ANSYS
export LSTC_LICENSE_SERVER=1055@ansys-ac.fraunhofer.de
export LM_PROJECT=LM_AC_220119

export perhost=12

PREF=NISSAN_log.$$
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
  wtim=24400
fi

echo time $wtime
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
export driver=ls-dyna_mpp_s_R12_0_0_x64_centos65_ifort160_avx2_intelmpi-2018_sharelib

cat << EOF > ${JDIR}/${SCRIPT}
#!/bin/csh -x
cd ${MYDIR}


# statements below probably not necessary for LSDYNA accessed via module load:
#module load intel/2018.02
# setenv KMP_AFFINITY compact
#module load intel
mpirun ${driver} I=${INPUTFILE} NCPU=1 MEMORY=${memory}  MEMORY2=${memory2}
EOF

# other partitions are possible
sbatch -N ${nnod}-${nnod} --partition=loewenburg --ntasks=${runnod} --exclusive -t ${hr}:${min}:${sec} ${JDIR}/${SCRIPT}

# as an alternative use reservation my_reservation, if active:
# sbatch -N ${nnod}-${nnod} --reservation=my_reservation --ntasks=${runnod} --exclusive -t ${hr}:${min}:${sec} ${JDIR}/${SCRIPT}
