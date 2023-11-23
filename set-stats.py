#!/usr/bin/env python3
import json
import sys
import os
import consts

if len(sys.argv) > 1 and sys.argv[1]:
	print(sys.argv)

	# Read stats file
	stats = {}
	if os.path.exists(consts.stats_file):
		try:
			with open(consts.stats_file, 'r') as file:
				stats = json.loads(file.read())
				file.close()
		except Exception:
			exit(1)

	project_path = sys.argv[1]
	if project_path in stats:
		stats[project_path] += 1
	else:
		stats[project_path] = 1

	# Save stats file
	try:
		with open(consts.stats_file, 'w') as file:
			file.write(json.dumps(stats))
			file.close()
	except Exception:
		exit(1)
    
