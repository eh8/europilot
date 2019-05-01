import os

# readFile and WriteFile from
# http://www.cs.cmu.edu/~112/notes/notes-strings.html


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


def findConfig():
    # Find the Euro Truck Simulator 2 directory in Documents
    home = os.path.expanduser('~')
    documents = os.path.join(home, 'Documents')
    euro = os.path.join(documents, 'Euro Truck Simulator 2')
    path = euro + '\config.cfg'
    # Open config.cfg
    return path


def checkDimensions():
    # See if the user has ran Jalopy before
    path = findConfig()
    config = readFile(path)
    result = ""
    for line in config.splitlines():
        # If anomaly detected in game parameters, then break immediately
        # and rewrite all settings
        if line.startswith('user r_mode_height'):
            if '600' not in line:
                return False
        elif line.startswith('user r_mode_width'):
            if '800' not in line:
                return False
        elif line.startswith('user r_fullscreen'):
            if '0' not in line:
                return False
    return True


def changeDimensions():
    # Change game parameters if not
    path = findConfig()
    config = readFile(path)
    result = ""
    for line in config.splitlines():
        if line.startswith('user r_mode_height'):
            lineToAdd = 'user r_mode_height "600"\n'
            result += lineToAdd
        elif line.startswith('user r_mode_width'):
            lineToAdd = 'user r_mode_width "800"\n'
            result += lineToAdd
        elif line.startswith('user r_fullscreen'):
            lineToAdd = 'user r_fullscreen "0"\n'
            result += lineToAdd
        else:
            line = line + '\n'
            result += line
    writeFile(path, result)