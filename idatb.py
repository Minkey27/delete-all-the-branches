#!/usr/bin/env python
"""
Interactively deleting all the branches.
"""
import sys

from git import Repo
from PyInquirer import prompt, style_from_dict, Token
from termcolor import colored


STYLE = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


repo_dir = sys.argv[1]

repo = Repo(repo_dir)

# Compile choices.
choices = []
for branch in repo.branches:
    choices.append({'name': branch.name})

# Compile data for pyinquirer.
prompt_data = [
    {
        'type': 'checkbox',
        'message': 'Select branches to delete locally.',
        'name': 'local branches',
        'choices': choices,
    },
]

# Prompt the thing.
answers = prompt(prompt_data, style=STYLE)

# Print the choices for confirmation.
for answer in answers['local branches']:
    print(colored(answer, 'red'))

# Prompt confirmation
cont = input(colored('Continue? (y/N)\n', 'green'))
if cont != 'y':
    print(colored('Try again. ¯\\_(ツ)_/¯'))
    sys.exit()

# Do the magic. :hurray:
for git_branch in answers['local branches']:
    if repo.active_branch.name == git_branch:
        print(colored('Can\'t delete current active branch \'%s\'' % git_branch, 'red'))
    else:
        print('Deleting locally: %s' % git_branch)
        repo.git.branch('-D', git_branch)
