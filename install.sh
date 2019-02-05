# create directory to store data
mkdir -p "$HOME/Documents/.script/misc"
installer_path="$(dirname ${BASH_SOURCE[0]})"
destination_path="$HOME/Documents/.script/misc"
script_name='splash.py'
script_identifier='alieff/graphic-splash'
alias_name='splash'

# copy the script 
if [[ -z "$(ls $destination_path | grep $script_name)" ]]; then 
  # copy source
  "cp" "$installer_path/$script_name" "$destination_path"
  echo "Copying done" : "cp $installer_path/$script_name" "$destination_path"
else # case if already installed
  echo 
  echo "$script_name executable is already exist"
  echo
fi

# register the script for auto source
if [ -z "$(cat $HOME/.bashrc | grep $script_identifier)" ] && [ $(alias "$alias_name"; echo $?) -eq 1 ]; then 
  # add identifier
  echo "# $script_identifier" >> $HOME/.bashrc
  # add auto source script
  "echo" "alias $alias_name='python $destination_path/$script_name'" >> $HOME/.bashrc
  echo "registering to bashrc done"
  echo "if you want to remove the alias just edit '$HOME/.bashrc'"
else # case if already installed
  echo 
  echo "$script_name auto source is already defined / alias already defined"
  echo
fi
