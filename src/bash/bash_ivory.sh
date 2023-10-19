# .bashrc
alias opn="nautilus -s ."
alias mc="/export/tools/MC_1.3.0.2/modelcompare/bin/mcompare.sh"
alias ansa="/export/tools/BETA_CAE_Systems/ansa_v19.1.6/ansa64.sh"
alias meta="/export/tools/BETA_CAE_Systems/meta_post_v19.1.6/meta_post64.sh"
alias gd="git add documents/* ; git commit -m 'documents'; git pull; git push"
#--------------------------------------------------------------------------------------------
export PATH=$HOME/usr/bin:$PATH
export LD_LIBRARY_PATH=$HOME/usr/lib64:$HOME/usr/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/usr/lib64/pkgconfig:$HOME/usr/lib/pkgconfig
#--------------------------------------------------------------------------------------------
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/apakiman/tools/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/apakiman/tools/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/apakiman/tools/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/apakiman/tools/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
#--------------------------------------------------------------------------------------------
export PATH=${HOME}/tools/vim/bin:$PATH

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
function set-title() {
  if [[ -z "$ORIG" ]]; then
    ORIG=$PS1
  fi
  TITLE="\[\e]2;$*\a\]"
  PS1=${ORIG}${TITLE}
}
PROMPT_COMMAND='echo -en "\033]0; $("pwd") \a"'
export PS1='${PWD##*/}:$ '
set-title '${PWD##*/}'
alias ll="ls -ltr"
#--------------------------------------------------------------
# shortcut path
#--------------------------------------------------------------
alias vwD="cd /export/AI_B_REDI_DATA"
alias pD="cd /export/PAG_DATA/VORDERWAGEN/002_Daten_Kaan"
alias work="cd /export/work/anahita"
#--------------------------------------------------------------
function djangoServer() {
	cd /export/work/web_dev/django_proj/ 
	conda activate ./envs
	cd cargraph
	set-title 'django-server'
       python manage.py runserver 129.26.129.242:8000
}
