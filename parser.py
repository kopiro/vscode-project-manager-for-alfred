import json
import sys
import os

BASE_DIR = 'Library/Application Support/Code/User/globalStorage/alefragnani.project-manager'
files = ['projects_cache_git.json', 'projects.json']

projects = []
for f in files:
    with open(os.path.join(os.path.expanduser('~'), BASE_DIR, f), 'r') as file:
        for p in json.loads(file.read()):
            p_path = p['fullPath'] if 'fullPath' in p else p['rootPath']
            projects.append({
                "title": p['name'],
                "subtitle": p_path,
                "arg": p_path
            })
projects = sorted(projects, key=lambda k: k['title'])

if len(sys.argv) > 1 and sys.argv[1]:
    projects = [e for e in projects if sys.argv[1].lower()
                in e['title'].lower()]

print(json.dumps({
    "items": projects
}))
