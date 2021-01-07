import subprocess
from pathlib import Path


def newsketch(name):
    try:
        path = Path.joinpath(Path().resolve(),"ArduinoSketches",name)
        subprocess.run(["arduino-cli","sketch","new",path])
    except:
        print("Error")


newsketch("test")
