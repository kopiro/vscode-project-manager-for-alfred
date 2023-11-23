#!/usr/bin/env bash

query=$1
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
code --folder-uri ${query}