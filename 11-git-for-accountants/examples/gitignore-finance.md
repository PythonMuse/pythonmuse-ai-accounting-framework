# .gitignore for Finance Projects

*What .gitignore does, why it matters, and a complete template for accounting AI projects.*

---

## What .gitignore Does

A `.gitignore` file tells Git which files and folders to exclude from version tracking. Any file that matches a pattern in `.gitignore` will not be committed to your repository.

Think of it as a "do not file" list for your workpaper binder.

---

## Why It Matters for Accounting

1. **Protect sensitive data.** Environment files with credentials, data files with PII, and configuration files with API keys should never be committed.
2. **Keep the repository clean.** Python cache files, IDE settings, and OS files clutter the repository and add no value.
3. **Avoid large files.** Excel files and database files can be massive. Git is designed for text files, not binary blobs.
4. **Prevent accidents.** Without a .gitignore, a careless `git add .` could commit a file with Social Security numbers.

---

## Complete .gitignore Template

```gitignore
# ===========================
# SENSITIVE DATA (CRITICAL)
# ===========================
# Never commit credentials, keys, or environment files
*.env
.env.*
credentials.*
secrets.*
*.pem
*.key
*.pfx

# ===========================
# FINANCIAL DATA
# ===========================
# Large data files should not be in version control
# Keep sample data tracked; exclude real data
data/raw/*.xlsx
data/raw/*.xls
*.db
*.sqlite
*.sqlite3
*.bak

# ===========================
# PYTHON
# ===========================
__pycache__/
*.py[cod]
*$py.class
*.so
*.egg-info/
dist/
build/
.eggs/
venv/
.venv/
env/

# ===========================
# IDE AND EDITOR
# ===========================
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
.idea/
*.swp
*.swo
*~

# ===========================
# OPERATING SYSTEM
# ===========================
.DS_Store
Thumbs.db
desktop.ini
ehthumbs.db

# ===========================
# JUPYTER NOTEBOOKS
# ===========================
.ipynb_checkpoints/

# ===========================
# LOGS
# ===========================
*.log
logs/
```

---

## How to Verify It Is Working

After creating your `.gitignore`, run:

```bash
git status
```

Files that match your `.gitignore` patterns should not appear in the output. If a file you expected to be ignored still shows up, check:

1. Is the pattern correct? (capitalization, path, wildcards)
2. Was the file already tracked before you added the rule? If so, you need to untrack it: `git rm --cached filename`

---

*Back to [Git for Accountants](../)*
