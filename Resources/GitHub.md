Of course! Here's the guide formatted in a student-friendly way:

---

# Student Guide: Submitting Code Changes with Git and GitHub

Hello! This guide will walk you through the process of making code changes, submitting them for review, and waiting for approval. Don't worry, it's easier than it sounds. Let's get started!

## 1. **Creating Your Own Working Branch**:


Create a branch to work in:

```bash
git checkout -b your-branch-name
```
> 🚀 Tip: Name your branch something descriptive about the changes you're making. For example, if you're working on a calculator project, you might name it `fix-calculator-divide-bug`.

## 2. **Make and Save Your Changes**:

This is where you code! After you've made your changes, you'll want to save (or "commit") them:

```bash
# This adds all of your changes to a staging area.
git add .

# This saves your staged changes along with a descriptive message.
git commit -m "Short description of the changes you made"
```

## 3. **Share Your Changes**:

Now, you'll push (or "upload") your changes to GitHub:

```bash
# This sends your branch and changes to GitHub. The first time you push your branch, you'll set its "upstream".
git push --set-upstream origin your-branch-name
```

If you've already set the upstream for this branch before, you can simply use:

```bash
git push
```

## 4. **Requesting Your Changes to be Reviewed**:

1. Go to the GitHub page of our class repository.
2. You'll likely see a notification suggesting you to create a pull request with the changes you just pushed. If so, click on **Compare & pull request**.
3. If you don't see the notification:
   - Click the **Pull requests** tab.
   - Then, click **New pull request**.
   - Make sure to select `main` for the "base" branch and `your-branch-name` for the "compare" branch.
4. Write a brief title and description for your pull request to explain your changes.
5. Click **Create pull request**.

Now your changes are submitted for review! 🎉

> 🌟 Note: Once you've submitted your pull request, you don't need to do anything else! Just wait for feedback or approval. If any changes are requested, you can make them in your branch, commit them, and push again. They'll automatically be added to your pull request.