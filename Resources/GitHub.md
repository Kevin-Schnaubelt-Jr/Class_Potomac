# Student Guide: Submitting Code Changes with Git and GitHub

Hello! This guide will help you navigate through making code changes, submitting them for review, and keeping your local code up-to-date. Let's dive in!

## 1. **Creating Your Own Working Branch**:



create a branch to work in:

```bash
git checkout -b your-branch-name
```
> 🚀 Tip: Choose a descriptive name for your branch. For instance, if you're working on a calculator project, consider `fix-calculator-divide-bug`.

## 2. **Make and Save Your Changes**:

Once you're ready to turn in your work, save (or "commit") them:

```bash
# This stages all your changes.
git add .

# This commits your staged changes with a message describing what you did.
git commit -m "Short description of the changes you made"
```

## 3. **Share Your Changes**:

Next, you'll upload (or "push") your changes to GitHub:

```bash
# This sends your branch and changes to GitHub. For the first-time push of this branch, set its "upstream".
git push --set-upstream origin your-branch-name
```

If you've pushed this branch before, simply use:

```bash
git push
```

## 4. **Requesting Your Changes to be Reviewed**:

1. Go to the GitHub page of our class repository.
2. You might see a suggestion to create a pull request for the changes you've just pushed. If so, click on **Compare & pull request**.
3. If not:
   - Head to the **Pull requests** tab.
   - Click **New pull request**.
   - Ensure the "base" branch is `main` and the "compare" branch is `your-branch-name`.
4. Write a brief title and description explaining your changes.
5. Hit **Create pull request**.

Your changes are now awaiting review! 🎉

## 5. **Updating Your Local Main After Approval**:

AFTER your pull request has been reviewed and merged:

1. Move back to your `main` branch:

```bash
git checkout main
```

2. Update it with the latest changes from the class repository:

```bash
git pull origin main
```

Now, your local `main` branch is up-to-date with all the latest approved changes.