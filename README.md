# Delete all the branches!

This is a simple PYTHON3 repo that prompts all your local branches so that you can select which branch you want to delete locally. Keep your workspace clean!

## Installation

Clone the repo and do the pip installs. Best do this in a virtualenv.

```bash
pip install -r requirements.txt
```

## Usage

```bash
# ./idatb.py <your_git_repo_dir>
./idatb.py /Users/yyung/projects/voipgrid-sandbox
```

Or if you do not supply an argument, it will get the current directory. Make sure you use the correct virtualenv. ;)
```bash
/Users/yyung/.virtualenvs/delete-all-the-branches/bin/python /Users/yyung/projects/delete-all-the-branches/idatb.py
```