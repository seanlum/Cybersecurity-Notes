echo 'Generating Untracked Files Index'
git ls-files --others --exclude-standard > untracked-files.txt
python3 create-readme.py