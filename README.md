# CodinGame puzzles and solutions

Those are my Python3 solutions for CodinGame puzzles

[For more info please visit CodinGame website](https://www.codingame.com)

### List of content

1. [CLASSIC PUZZLE - EASY (Python 3)](https://github.com/ikostan/CodinGame/tree/master/CLASSIC_PUZZLE_EASY)

### Setting up Python3 virtual environment on Windows machine:

1. open CMD
2. navigate to project directory, for example:<br/> 
```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```
3. run following command:<br/> 
```bash 
pip install virtualenv
```
4. run following command:<br/> 
```bash 
virtualenv venv --python=python
```

### How to delete multiples files in Git:

- In the command-line, navigate to your local repository.
- Ensure you are in the default branch:<br/> 
```bash 
git checkout master
```
- The rm -r command will recursively remove your folder:<br/> 
```bash 
git rm -r folder-name
```
- Commit the change:<br/> 
```bash 
git commit -m "Remove duplicated directory"
```
- Push the change to your remote repository:<br/> 
```bash 
git push origin master
```

### How to fix in case .gitignore is ignored by Git:
Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 
**NOTE:** First commit your current changes, or you will lose them.<br/> 
Then run the following commands from the top folder of your Git repository:<br/> 
```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```

### More help:
[pip nstallation and upgrade](https://pip.pypa.io/en/stable/installing/)

<p align="center"> 
<img src="https://github.com/ikostan/CodinGame/blob/master/codingame_img.png">
</p>
<!--![CodinGame Logo](https://github.com/ikostan/CodinGame/blob/master/codingame_img.png?style=center)-->
