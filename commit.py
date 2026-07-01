import os
from datetime import datetime

for i in range(5):
    with open("contribution.txt", "a") as f:
        f.write(f"{i} {datetime.now()}\n")

    os.system("git add contribution.txt")
    os.system(f'git commit -m "Commit {i+1}"')

os.system("git push origin main")