# Your First Repository: A Step-by-Step Walkthrough

*From zero to a working Git repository in 15 minutes.*

---

## Prerequisites

- Git installed ([https://git-scm.com/](https://git-scm.com/))
- A GitHub account ([https://github.com/](https://github.com/))
- VS Code (optional but recommended)

---

## Step 1: Configure Git (One-Time Setup)

Open a terminal and set your name and email. This identifies you in the commit history.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**What this does:** Every commit you make will be tagged with this name and email. Think of it like the "Prepared By" field on a workpaper.

---

## Step 2: Create a Project Folder

```bash
mkdir my-first-project
cd my-first-project
```

**What this does:** Creates a new empty folder and moves into it.

---

## Step 3: Initialize Git

```bash
git init
```

**What this does:** Tells Git to start tracking this folder. Git creates a hidden `.git` folder where it stores all history. You will never need to open this folder directly.

---

## Step 4: Create Your First File

```bash
echo "# My First Project" > README.md
echo "This is a test project for learning Git." >> README.md
```

Or open the folder in VS Code and create `README.md` manually.

---

## Step 5: Check Status

```bash
git status
```

**What you see:** Git shows `README.md` as an "untracked file." This means Git sees the file but is not tracking it yet.

**Accounting analogy:** You have a document on your desk, but it has not been filed yet.

---

## Step 6: Stage the File

```bash
git add README.md
```

**What this does:** Tells Git you want to include this file in the next commit.

**Accounting analogy:** You have put the document in the "to be filed" tray.

---

## Step 7: Commit

```bash
git commit -m "Initialize project with README"
```

**What this does:** Creates a permanent snapshot of your project at this moment, with a description of what you did.

**Accounting analogy:** You have filed the document with a description on the cover sheet.

---

## Step 8: Create a Repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Name your repository (e.g., `my-first-project`)
3. Leave it empty (do not add a README on GitHub -- you already have one)
4. Click "Create repository"
5. GitHub will show you commands to connect your local project

---

## Step 9: Connect Local to Remote

Copy the commands GitHub showed you. They will look something like:

```bash
git remote add origin https://github.com/your-username/my-first-project.git
git branch -M main
git push -u origin main
```

**What this does:**
- `remote add origin` connects your local folder to GitHub
- `branch -M main` renames your default branch to `main`
- `push -u origin main` sends your local commits to GitHub

---

## Step 10: Verify

Go to your GitHub repository page. You should see your `README.md` file.

Run `git status` locally. It should show "nothing to commit, working tree clean."

You now have a working Git repository with a remote backup on GitHub.

---

## What to Do If Something Goes Wrong

**"Permission denied" when pushing:**
You may need to set up authentication. GitHub supports personal access tokens and SSH keys. The simplest method: [GitHub CLI](https://cli.github.com/) with `gh auth login`.

**"Not a git repository" error:**
Make sure you ran `git init` in the correct folder. Check with `pwd` (print working directory).

**Accidentally committed a file you should not have:**
Remove it from tracking (but keep the local file): `git rm --cached filename`

**Committed with the wrong message:**
Amend the most recent commit: `git commit --amend -m "Corrected message"`

---

## Next Steps

1. Add more files to your project (plan.md, a data folder, etc.)
2. Make changes and commit regularly
3. Explore `git log` to see your history
4. Try the [folder structure template](../08-project-hygiene/templates/folder-structure-template.md) for your next real project

---

*Back to [Git for Accountants](../)*
