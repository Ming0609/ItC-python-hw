# ItC-python-hw
Introduction to computer python homework: crawl news from website

# Author
yang611
Ming
matdexir

# Development SOP
Master branch is protected so you have to open you new branch
and develop on it. After your work is done, you can push the 
new branch to github, and pull request. When reviews on the 
new request is done, the branch will be merged.

### 
# copy from github
git fetch
git merge origin/master # merge current local branch to origin/master

# open new branch
git branch BRANCH_NAME
git checkout BRANCH_NAME # change current position to new branch


# After making some changes you have to commit your changes
git add .
git commit -m "commit massage"

# repository might be changed after your fetch
git fetch
git rebase origin/master

# if some conflicts happen, you have to fix it and
git rebase --continue

# after all conflicts are fixed, push your branch to github
git push -u origin BRANCH_NAME

then go to github website and click "pull requests"
### 

