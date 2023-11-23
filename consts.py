#!/usr/bin/env python3
import os

BASE_DIR = os.path.join(os.path.expanduser('~'), 'Library/Application Support/Code/User/globalStorage/alefragnani.project-manager')
project_manager_json_files = ['projects_cache_git.json', 'projects.json']
stats_file = os.path.join(BASE_DIR, 'alfred_stats.json')
