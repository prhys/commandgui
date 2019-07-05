#!/usr/bin/env bash

#Description = This command will turn plain text files (like .txt) made in Linux into a format that can be read on Windows

#Danger = None

#Risks = None

#Commands
awk 'sub("$", "\r")' "$1" > "$2"
exit "$?"