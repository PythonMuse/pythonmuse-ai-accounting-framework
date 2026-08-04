# Your Workspace -- VS Code as the Worked Example

*Think of it as Windows Explorer for your AI workflows -- where files live, logic runs, and outputs are stored.*

---

## Why VS Code

Visual Studio Code is a free, Microsoft-backed code editor that has become the standard workspace for working with AI tools. For accountants, it is not about writing code from scratch. It is about having a single place where:

- Your project files are organized and visible
- AI assistants can read and write files
- You can run Python scripts with one click
- You can review changes and track versions
- Everything is in one window instead of scattered across applications

Think of it as the difference between having your reconciliation workpapers spread across five folders and email threads versus having them organized in a single binder.

> **A note on tools.** VS Code is the worked example throughout this framework because it is free, widely approved, and works with every major AI assistant. The framework is not specific to it. Cursor, Windsurf, JetBrains, and the terminal-based tools all work the same way. What matters is that your files, your instructions, and your AI are in one place. See [Module 14](../14-ai-work-harness/) for what that arrangement is actually called.

---

## The VS Code Layout

When you open VS Code, you will see four main areas:

**Sidebar (left):** Your file explorer. Shows all the files and folders in your project. Click to open any file.

**Editor (center):** Where you view and edit files. You can have multiple files open in tabs, just like browser tabs.

**Terminal (bottom):** A command line built into VS Code. This is where you run Python scripts, Git commands, and other tools without leaving the application.

**Extensions (left bar icons):** Add-ons that extend VS Code's capabilities. Think of them as apps for your workspace.

---

## Your First 15 Minutes in VS Code

### Step 1: Install VS Code

Download from [https://code.visualstudio.com/](https://code.visualstudio.com/). It is free and supported on Windows, Mac, and Linux.

### Step 2: Open a Project Folder

Go to File > Open Folder and select the folder where your project lives (or create a new one).

This is important: VS Code works with folders, not individual files. When you open a folder, everything inside it becomes your workspace.

### Step 3: Create a File

Right-click in the sidebar and select "New File." Name it `plan.md`. Type a few lines of Markdown. You now have your first project file.

### Step 4: Open the Terminal

Press `` Ctrl+` `` (the backtick key, usually above Tab). The terminal panel opens at the bottom. This is where you will run scripts.

### Step 5: Install Python Extension

Click the Extensions icon in the left bar (it looks like four squares). Search for "Python" and install the one by Microsoft. This enables Python support, syntax highlighting, and the ability to run scripts directly.

### Step 6: Run a Script

If you have a Python script (for example, from the [Python Without Intimidation](../03-python-without-intimidation/) section), open it in the editor and press the play button in the top right. Or type `python your_script.py` in the terminal.

---

## Why VS Code Over Other Tools

| Feature | VS Code | Excel | Notepad | Word |
|---------|---------|-------|---------|------|
| File organization | Full project view | Single file | Single file | Single file |
| AI integration | Built-in support | Limited | None | Limited |
| Python support | Full | None | None | None |
| Version control (Git) | Built-in | None | None | Track Changes only |
| Terminal access | Built-in | None | None | None |
| Markdown preview | Built-in | None | None | None |
| Free | Yes | Requires license | Yes | Requires license |

---

## Extensions Are Software Vendors

An extension is a third-party add-on that runs inside your workspace, with the access your workspace has. Installing one is a vendor decision, not a preference.

Five questions before you install anything:

1. **Who built it?** Look for a verified publisher badge. "Claude AI Assistant" is not necessarily Anthropic -- name impersonation in extension marketplaces is common.
2. **How many people use it?** Install counts and reviews can be forged, so treat a high number as one signal rather than proof.
3. **Is it open source?** Helpful, not sufficient. The XZ Utils backdoor in 2024 was in open source that thousands of people could read.
4. **What does it actually do?** If the description does not explain the permissions it wants, that is the answer.
5. **Is it actively maintained?** Last updated 2021 means unpatched.

**Minimalism is a control.** Every extension is operational surface area. The fewer you run, the less there is to review, patch, and explain.

| Extension | Publisher | Why |
|---|---|---|
| Python | Microsoft | Run and debug scripts |
| GitHub Copilot | GitHub | AI assistance inside the editor |
| Markdown All in One | Yu Zhang | Preview and shortcuts |

See [approved-extensions-template.md](examples/approved-extensions-template.md) for a template to track what your team has approved and why.

---

## Key Concepts for Accountants

### The Workspace = Your Engagement Folder

When you open a folder in VS Code, that folder becomes your workspace. Everything inside it is visible and accessible. This is your project boundary -- like an engagement folder that contains all the workpapers, data, and outputs for a specific project.

### The Terminal = Your Command Line

The terminal is where you run things. You do not need to memorize complex commands. The most common ones:

```bash
python script_name.py          # Run a Python script
git status                     # See what files have changed
git add .                      # Stage changes
git commit -m "description"    # Save a checkpoint
```

### Files and Folders = Your Organizational Structure

VS Code makes it easy to see and manage your project structure. A well-organized project might look like:

```
my-project/
  CLAUDE.md
  plan.md
  status_update.md
  data/
    raw/
    processed/
  outputs/
  src/
```

You can create, rename, move, and delete files directly in the sidebar.

---

## Tips for Getting Comfortable

1. **Start with Markdown.** Before you touch Python or AI, just use VS Code to write Markdown files. Get comfortable with the editor.

2. **Use the preview.** Press `Ctrl+Shift+V` to preview a Markdown file. You can see the formatted version side by side with the source.

3. **Use keyboard shortcuts.** `Ctrl+S` to save, `Ctrl+P` to quick-open any file by name, `` Ctrl+` `` to toggle the terminal.

4. **Do not worry about customization.** The default settings are fine. You can adjust things later as you develop preferences.

5. **Let the AI help.** If you install an AI extension (Claude, Copilot), it can help you navigate VS Code itself. Ask it "How do I split the editor?" or "How do I search across files?"

---

## Next Steps

Once you are comfortable with the basics:

- Install the recommended extensions listed in [recommended-extensions.md](examples/recommended-extensions.md)
- Open one of the example projects from this framework
- Try running a Python script from the terminal

---

*Next: [AI Permissions](../05-ai-permissions/) -- understanding what AI tools can access.*
