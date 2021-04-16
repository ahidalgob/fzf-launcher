#!/bin/python
"""Entry point for fzf-launcher."""
import sys
import os
from subprocess import run, PIPE

sys.path.append(f'{os.getenv("HOME")}/.config/fzf-launcher/')
scripts = os.path.dirname(os.path.realpath(__file__)) + "/scripts"

from config import commands


def launch() -> None:
    if "--wrapper" in sys.argv:
        run(
            "alacritty --class=Alacritty,FzfLauncher -e "
            "python ~/Projects/fzf-launcher/fzf_launcher.py & disown",
            shell=True)
        return

    dmenu_path = run(f"{scripts}/getallinpath.sh", shell=True, stdin=PIPE, stdout=PIPE)
    commands_in_path = {c: c for c in dmenu_path.stdout.decode().strip().split()}
    final_commands = { **commands, **commands_in_path}

    tags = "\n".join(list(final_commands.keys()))

    c = run(f"echo \"{tags}\" | fzf --no-info", shell=True, stdin=PIPE, stdout=PIPE)
    tag = c.stdout.decode().strip()
    if tag != "":
        command = final_commands[tag]
        if isinstance(command, str):
            command = [command]
        for c in command:
            run(f'nohup {c} &', shell=True)


if __name__ == "__main__":
    launch()
