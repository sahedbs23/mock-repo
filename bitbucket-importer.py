# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/sawon/var/www/html/123rf-payments")
# Your mock repo
mock_repo = git.Repo("/Users/sawon/var/www/html/mock-repo")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['ssawon.bs23@gmail.com', 'sahed.moral@123rf.com'])
importer.import_repository()