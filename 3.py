# py -m venv "virtual environment name" <- to create virtual environment
# source "virtual environment name"/bin/activate <- to activate virtual environment
# ctrl + shift + p -> python interpreter -> select workspace (It will automatically activate the virutal environment whenever you open the particular folder/ project)


# git restore "file name" <- ( This command restore deleted file)
# git pull <- (This command download/pull the new file in local environment)

# Create branch
# git branch --help <- (gives documentation about branch)
# git branch --list <- (Listing branch you created)
# git branch "branch name" <- (create new branch)
# git checkout "branch name" <- (switches to the given branch name)
# git checkout -b "branch name" <- (create new branch and switch to it)
# git branch -d "branch name" <- (delete branch)
# git branch -D "branch name" <- (delete branch forcefully)
# git merge "branch name" <- (merge branch with current branch)
# git merge --abort <- (abort merge)
# git merge --continue <- (continue merge)
# git merge --no-commit <- (merge branch without commit)
# git branch -M main <- (rename the branch name to main 
# git push -u origin main <- (intitialising main branch for every push operation)
# git diff branch name <- (to compare commit, branches, files & more)
# git pull origin main <- ( used to fetch and download content from a remote repo and immediately update
# the local repo to match the content).

# Undoing Changes

'''Case 1 : Staged changes (add .)

git reset <- file name -> <-(reset one file)
git reset <- (reset many files)

'''

''' Case 2: commited changes (for one commit)
  
  git reset HEAD~1
'''

''' Case 3 : commited changes( for many commits)

git reset <- commit hash ->
git reset --hard <- commit hash -> (reset changes even from local repo)
'''

#git restore <filename> <- (restore deleted file)
# git restore <file1> <file2> ...  <- (restore multiple deleted files)

# git log <- (checks all the history of commits)

# Fork

''' A fork is a new repo that shares code nad visibility settings with 
the original "upstream" repository'''

# Fork is a rough copy
# clone is a exact copy
