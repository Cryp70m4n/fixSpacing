import os

tragetDir = "."
blacklist = ["fixSpacing.py"]

def fixSpacing(targetFile: str) -> None:
    ignore = False
    symbolTable = ["=", "!"]
    src = []
    source = ""

    with open(targetFile, "r") as f:
        for line in f:
            for char in line:
                src.append(char)

    for index, symbol in enumerate(src):
        if any(flag == symbol for flag in ["'", '"']):
            ignore = not ignore
        if symbol in symbolTable and not ignore:
            if all(symbol != src[index-1] for symbol in [" ", "=", "!"]):
                if any(symbol == src[index-1] for symbol in ["+", "-", "/", "*"]):
                    source = source[:-1] + " " + source[-1:]
                else:
                    symbol = " " + symbol

            if all(symbol != src[index+1] for symbol in [" ", "=", "!", "+", "-", "/", "*"]):
                symbol += " "

        source += symbol

    with open(targetFile, "w") as f:
        f.write(source)

files = os.listdir(tragetDir)

for file in files:
    if file not in blacklist:
        fixSpacing(file)