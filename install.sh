#!/bin/bash
clear
echo "#!/bin/bash 
python james.py" '${1+"$@"}' > james;
chmod +x james;
sudo cp james /usr/bin;
