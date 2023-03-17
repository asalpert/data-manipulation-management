# CSE314A SP23 Assignments

This repository contains template code for the assignments in the course. It will additionally serve as an _upstream repository_ to source potential updates and corrections for the assignments.

<<<<<<< HEAD
To check out a newly posted assignment branch, run:

```
git fetch upstream
git switch -t upstream/hw1
=======
Follow the steps at [Setting Up Your Private Repo](https://wustl-data.github.io/sp23/dev_env/private_repo) to get started using this repo.

To check out a newly posted assignment branch, run:

```
git fetch upstream
git switch -t upstream/hw3-u
```

It is advised to continue your work on a separate branch that tracks your `origin` repository instead of upstream:

```
git switch -c hw3
git push -u origin hw3
```

To integrate updates to the assignment from upstream, then you may do the following:
```
git switch hw3-u
git pull
git switch hw3
git merge hw3-u
>>>>>>> main
```

Assuming you've set up your repo according to one of our suggested [dev environment setups](https://wustl-data.github.io/sp23/Development%20Environment/choose_env), you may now instantly pull the latest updates and corrections from an `upstream` branch to make sure your code is up-to-date. With the branch you'd like to update checked out, simply run:

<<<<<<< HEAD
```
git pull
```

> If you've failed to set `upstream` as the tracking branch, `git pull` will try to fetch changes from `origin` as the default. If this is the case, you can either set `upstream/hw1` as the tracking branch with `git branch -u upstream hw1` or just specify the remote when you pull with `git pull upstream`.

See our course page on our [Development Environment](https://wustl-data.github.io/sp23/devenv) for more information on how our git workflow is configured.

## Autograder

Our autograder is simply a GitHub Action that runs the tests in your code. Run the command `pytest` to try out these tests locally. The GitHub Action currently runs any time you push the code to GitHub. I am configuring our setup to only run the autograder on designated submission branches to reduce the noise of unnecessary test runs-- stay tuned for updates.
=======
> If your tracking branches are different than the approach suggested here, you may have to manually specify the correct repositories and/or branches in the commands above. Use the help command to help you, e.g. `git pull -h`

See our course page on our [Development Environment](https://wustl-data.github.io/sp23/devenv) for more information on how our git workflow is configured.

## Autograder

Our autograder is simply a GitHub Action that runs the tests in your code. Run the command `pytest` to try out these tests locally. The GitHub Action (if configured) runs any time you push the code to GitHub.
>>>>>>> main
