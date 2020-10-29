from distutils.core import setup

import py2exe
import glob

setup(
    # this is the file that is run when you start the game from the command line.
    console=["main.py"],
    # data files - these are the non-python files, like images and sounds
    data_files=[
        ("sprites", glob.glob("sprites\\*.json")),
        ("sfx", glob.glob("sfx\\*.ogg") + glob.glob("sfx\\*.wav")),
        ("levels", glob.glob("levels\\*.json")),
        ("img", glob.glob("img\\*.gif") + glob.glob("img\\*.png")),
        ("", ["settings.json"]),
    ],
)
