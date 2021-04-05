
Requirements:
- alacritty
- fzf


Config:
Write a python file (~/.config/fzf-launcher/config.py) that defines a list of pairs (tag, command) named "commands"

```python
commands = {
    "uh oh": "playerctl -p spotify open spotify:album:3PzrNuMGWGpp8WOfrmpkaU"
}
```
