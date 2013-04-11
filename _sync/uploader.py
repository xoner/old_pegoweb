'''
This module updates the contents of the website depending on the changes present on the jekyll
repository.
'''
from git import *
from os import path

def main():
    repo= Repo('..')

    markdown_ext = ('.markdown', '.md')
    ignored_dirs = ('_extensions', '_sync')

    # Get the repository changes.
    repo_changes = []
    for change in repo.index.diff(None):
        file_path = change.a_blob.path
        if path.dirname(file_path) not in ignored_dirs:
            repo_changes.append(file_path)

    for untracked_file in repo.untracked_files:
        if path.dirname(untracked_file) not in ignored_dirs:
            repo_changes.append(untracked_file)

    pending_uploads = []
    for change in repo_changes:
        if '_post' in path.dirname(change):
            pass
        if '_layouts' in path.dirname(change):
        elif path.splitext(path.basename(change))[1] in markdown_ext:
            pass
        else


if __name__ == '__main__':
    main()