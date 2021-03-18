#!/bin/bash
command="$(python ~/Projects/fzf-launcher/fzf_launcher.py $(python ~/Projects/fzf-launcher/fzf_launcher.py | fzf))"
bash -c "$command"
