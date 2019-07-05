#!/usr/bin/env bash

#Description = This command will turn plain text files (like .txt) made in Windows into a Linux format

#Danger = None

#Risks = None

#Commands
awk '{ sub("\r$", ""); print }' "$1" > "$2"
exit "$?"
