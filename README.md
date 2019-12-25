# ItC-python-hw
Introduction to computer python homework: crawl news from website

## Teamname - 你各位會不會用git啊

## Author, ID, github
許晉洋, B05203017, yang611
沈世明, ,Ming0609
Matdexir, B08209032, matdexir

## Introduction
A simple Crawler that crawls announcement from csie website and parse it into a csv file

## Environment
macOS Mojave 10.14.3 (work fine in linux, too)
lxml==4.4.2
requests==2.22.0
python==3.7.2

note: you can use ```pip install -r requirement.txt``` to install package
## collaboration contribution
- 許晉洋: 
In Programming part, I worked on argument parser and Crawl_page(), Crawl_content() function,
which parse the html then return.
Also, I wrote a simple git guide below for our team.

- 沈世明:
I worked on the crawler.py part of the program which send the request to the web and I also find the xpath of the content.

- Matdexir:
I worked on the main.py part of the program which saves the output from the crawler in a csv format file.

## Development SOP
Master branch is protected so you have to open you new branch
and develop on it. After your work is done, you can push the 
new branch to github, and pull request. When reviews on the 
new request is done, the branch will be merged.


#### copy from github
git fetch
git merge origin/master # merge current local branch to origin/master

#### open new branch
git branch BRANCH_NAME
git checkout BRANCH_NAME # change current position to new branch


#### After making some changes you have to commit your changes
git add .
git commit -m "commit massage"

#### repository might be changed after your fetch
git fetch
git rebase origin/master

#### if some conflicts happen, you have to fix it and
git rebase --continue

#### after all conflicts are fixed, push your branch to github
git push -u origin BRANCH_NAME
then go to github website and click "pull requests"

