#!/usr/bin/env python3
import json
import sys
import os
import consts

# Read stats file
stats = {}
if os.path.exists(consts.stats_file):
	try:
		with open(consts.stats_file, 'r') as file:
			stats = json.loads(file.read())
			file.close()
	except Exception:
		pass

projects = []
for json_file in consts.project_manager_json_files:
	full_path_json_file = os.path.join(consts.BASE_DIR, json_file)
	if os.path.exists(full_path_json_file):
		try:
			with open(full_path_json_file, 'r') as file:
				for p in json.loads(file.read()):
					project_path = p['fullPath'] if 'fullPath' in p else p['rootPath']
					projects.append({
						"title": p['name'],
						"subtitle": project_path,
						"arg": project_path
					})
				file.close()
		except Exception:
			pass

# Sort by stats and then by title
projects = sorted(projects, key=lambda k: (-int(stats[k['arg']]) if k['arg'] in stats else 0, k['title']))

# Filter by query
if len(sys.argv) > 1 and sys.argv[1]:
	query = sys.argv[1].lower()
	projects = [p for p in projects if query in p['title'].lower() or query in p['subtitle'].lower()]

print(json.dumps({
	"items": projects
}))
