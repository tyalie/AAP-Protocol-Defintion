#!/usr/bin/env python3
import os
from pathlib import Path
import tempfile
import readline
import subprocess 
import re

folder=Path("examples")
data_file_type="data"
desc_file_type="md"

def get_free_filename(filename):
    number = 0
    while True:
        name = f"{filename}-{number:02}"
        if any((folder / f"{name}.{end}").exists() for end in [data_file_type, desc_file_type]):
            number += 1
        else:
            break

    return name



class FileCompleter:
    def __init__(self, folder: Path):
        filenames = set()
        for f in folder.glob("**/*"):
            if (m := re.match("^(.+)-\d+$", f.stem)):
                filenames.add(m.group(1))
        self.options = sorted(filenames)
        self.matches = []

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:
                self.matches = self.options[:]

        if state < len(self.matches):
            return self.matches[state]
        return None

# enable file completion
readline.set_completer(FileCompleter(folder).complete)
readline.set_auto_history(False)
readline.parse_and_bind('tab: complete')

filename = input("Filename\n> ").strip()
filename = get_free_filename(filename)

# disable completion
readline.parse_and_bind("set disable-completion on")  

print("-"*20)

print("Data (Hex)")
while True:
    data = input("> ").strip()
    if len(data) % 2 == 0 and re.match(r"^[\da-f]+$", data.lower()):
        break
    print("invalid input")
    
data_b = bytes(int(data[i:i+2], 16) for i in range(0, len(data), 2))

print("-"*20)

print("Description")
with tempfile.NamedTemporaryFile(mode="r", suffix=f".{desc_file_type}") as tf:
    subprocess.call(["editor", tf.name])

    tf.seek(0)
    description = tf.read()


print()
print("-"*20)
print(f"Storing '{filename}' with data:")
width = 20
print("-"*(width*3))
for i in range(0, len(data_b), width):
    print(" ".join(f"{d:02X}" for d in data_b[i:i+width]))
print("-"*(width*3))
print(f"Description")
print('\n'.join(f"| {a}" for a in description.split("\n")))

accept = input("correct? [Y/n]: ")

if not (len(accept) == 0 or accept.lower().strip() == "y"):
    print("Aborted")
    exit()


with open(folder / f"{filename}.{data_file_type}", "wb") as f:
    f.write(data_b)

with open(folder / f"{filename}.{desc_file_type}", "w") as f:
    f.write(description)
