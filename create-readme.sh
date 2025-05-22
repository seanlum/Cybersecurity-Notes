echo 'Generating Untracked Files Index'
git status --porcelain | grep '^??' | cut -c4- > untracked-files.txt
python3 create-readme.py