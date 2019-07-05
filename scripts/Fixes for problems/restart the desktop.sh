#!/usr/bin/env bash

#Description = This command will restart the desktop

#Danger = Low

#Risks = 

#Commands
systemctl restart lightdm
exit "$?"
