#!/bin/python
"""Entry point for fzf-launcher."""
import sys
import os
from subprocess import run, PIPE

sys.path.append(f'{os.getenv("HOME")}/.config/fzf-launcher/')
from config import commands


def launch() -> None:
    if "--wrapper" in sys.argv:
        run(
            "alacritty --class=Alacritty,FzfLauncher -e "
            "python ~/Projects/fzf-launcher/fzf_launcher.py & disown",
            shell=True)
        return

    tags = "\n".join(list(commands.keys()))
    c = run(f"echo \"{tags}\" | fzf", shell=True, stdin=PIPE, stdout=PIPE)
    tag = c.stdout.decode().strip()
    if tag != "":
        command = commands[tag]
        if isinstance(command, str):
            command = [command]
        else:
            for c in command:
                run(f'nohup {c} &', shell=True)


if __name__ == "__main__":
    launch()
