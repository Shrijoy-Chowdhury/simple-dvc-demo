create virtual environment
''' bash
conda create -n wineq python=3.8 -y
'''
create requirements file
install the requirements
'''bash
pip install -r requirements.txt
'''

Download data from https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

create the list of directories and files to be created and create them using the os command

git init

dvc init

dvc add data_given /winequality.csv

#add all data to git
git add .
git commit -m "first commit"

create a remote repository in the github before push the changes to git