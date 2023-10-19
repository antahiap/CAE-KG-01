#########
# files
########
export PS1='${PWD##*/}:$ '
PROMPT_COMMAND='echo -en "\033]0; $("pwd") \a"'

export PATH=$HOME/usr/bin:$PATH
export LD_LIBRARY_PATH=$HOME/usr/lib64:$HOME/usr/lib:/home/ndv/tools/DesParO-version3/DesParO_3_0_centos8_lin64/lib/:$LD_LIBRARY_PATH

export PKG_CONFIG_PATH=$HOME/usr/lib64/pkgconfig:$HOME/usr/lib/pkgconfig
export NODEJS_HOME=$HOME/usr/src/node-v12.16.3-linux-x64
export PATH=$PATH:$NODEJS_HOME/bin

alias f1="cd /home/ndv/data/TruckData"
alias a4="/home/ndv/tools/Animator_2.3.0/a4_v2.3.0_install_linux64/a4 -osm"
alias dv="/home/ndv/code/bin/dataviewer_linux64"
alias pv="~/tools/ParaView-5.7.0-MPI-Linux-Python3.7-64bit/bin/paraview"
alias cmake="~/tools/cmake-3.16.0-rc3-Linux-x86_64/bin/cmake"
alias qt="~/tools/qtcreator-3.6.0/bin/qtcreator"
alias loco="~/tools/loco/loco2-scale-v1.127.0-rhel7-x86_64.bin --disable-platform-check --disable-ssl-verify"
#alias loco="~/tools/loco/loco2-scale-v1.103.1-rhel7-x86_64.bin --disable-platform-check --disable-ssl-verify"
alias loco_test="~/tools/loco/loco2-scale-v1.103.1-rhel7-x86_64.bin --disable-platform-check --disable-ssl-verify --environment=test"
alias mendeley="~/usr/src/mendeleydesktop-1.19.4-linux-x86_64/bin/mendeleydesktop"
alias opn='nautilus -s .'
alias ap='cd /home/apakiman/Nextcloud/Projects/carGraph/02_simple_KG/keras_neo4j' #active project
alias cg='cd /home/apakiman/Nextcloud/Projects/carGraph/' #cargraph
alias runs="cd ~/Projects/carGraph/runs"
alias food="python /home/apakiman/Nextcloud/Projects/self_project/food/shope.py"


alias ll="ls -ltr"
function lex { find . -type f |perl -ne 'print $1 if m/\.([^.\/]+)$/' | sort -u; }
export -f lex

#alias win="xfreerdp /d:WASA  /bpp:24 /w:1920 /h:1200 +multitransport +clipboard +fonts /network:lan /sound:sys:pulse /v:spike /smartcard " #/sound:latency:400 +toggle-fullscreen 
alias win="xfreerdp /d:WASA  /bpp:24 /w:2560 /h:1400 +multitransport +clipboard +fonts /network:lan /sound:sys:pulse /v:spike /smartcard " #/sound:latency:400 +toggle-fullscreen 
alias a4lic="bash /home/ndv/code/gns_rlm_v12.4_R1_install_linux64/checkstatus.sh"

set -o vi
# BETA
#---------------------------------------------
source /home/compeng/config/env_beta_cae19.1.sh
alias ansa="vglrun -d /dev/dri/card1 ansa64.sh"
alias meta="vglrun -d /dev/dri/card1 meta_post64.sh"
#---------------------------------------------

export PATH=${HOME}/tools/vim/bin:$PATH

#[ -f ~/.fzf.bash ] && source ~/.fzf.bash
mvBack(){
echo $PWD/$1;scp -r $PWD/$1 apakiman@leo1:$PWD/$1/
#echo $PWD/$1;rsync -p $PWD/$1 apakiman@leo1:$PWD/$1/..
}

alias postManual="/home/apakiman/Projects/carGraph/prepost/script/postManual.sh"
#CUDA Environment Setup
export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

#conda activate pyg; cd Projects/kg01/; source envs/bin/activate; cd transferDOE;
function filter () {
    sed -i 's/cmidrule\\DIFaddFL{\((.*)\)}{\\DIFaddFL{\(.*\)}}/cmidrule\1{\2}/g' $1
}
#---------------------------------------------
function set-title() {  
	if [[ -z "$ORIG" ]]; then 
		ORIG=$PS1
	fi
	TITLE="\[\e]2;$*\a\]"
	PS1=${ORIG}${TITLE} 
}
export PS1='${PWD##*/}:$ '
set-title '${PWD##*/}' 

#---------------------------------------------
KG01(){
cd /home/apakiman/Nextcloud/Projects/carGraph/03_KG01;
conda activate ./envs;
set-title;
conda info --envs;
}

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
#---------------------------------------------
# new os
#module load texlive/2020
module load texlive
module load Java/13.0.2
#~/Stretchly-1.9.0.AppImage
clear
alias pycharm="/home/apakiman/tools/pycharm-community-2023.1.3/bin/pycharm.sh"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/apakiman/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/apakiman/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/apakiman/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/apakiman/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

