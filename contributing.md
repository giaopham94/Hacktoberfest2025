
# Contribution Rules📚:

- You are allowed to make pull requests that break the rules. We just merge it ;)
- Do NOT add any build steps e.g npm install (we want to keep this a simple static site)
- Do NOT remove other content.
- Styling/code can be pretty, ugly or stupid, big or small as long as it works
- Add your name to the contributorsList file
- Try to keep pull requests small to minimize merge conflicts


# Getting  Started 🤩🤗:

Fork this repo (button on top)
Clone to your local machine:
git clone https://github.com/muhtalhakhan/Hacktoberfest2025.git

Navigate to project directory:
cd Hacktoberfest2025

Create a new branch:
git checkout -b my-new-branch

Add your contributions (UI/content changes)

Stage and commit your changes:
git add .
git commit -m "Updated contributor guide and documentation fixes"

Push to your branch:
git push origin my-new-branch

Create a pull request 🚀

## Avoid Conflicts {Syncing your fork}

An easy way to avoid conflicts is to add an 'upstream' for your git repo, as other PR's may be merged while you're working on your branch/fork.   

```terminal
git remote add upstream https://github.com/muhtalhakhan/Hacktoberfest2025.git
```

You can verify that the new remote has been added by typing
```terminal
git remote -v
```

To pull any new changes from your parent repo simply run
```terminal
git merge upstream/master
```

This will give you any eventual conflicts and allow you to easily solve them in your repo. It's a good idea to use it frequently in between your own commits to make sure that your repo is up to date with its parent.
