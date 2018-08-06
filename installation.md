## Installation

*Note:* Python 3.6 or higher can be used for this workshop.

### Windows

#### Text editor
You can use [Notepad++](https://notepad-plus-plus.org/download/v7.5.8.html), [Atom](https://atom.io), [Sublime Text](http://www.sublimetext.com) or other text editor of your choice.

#### GitBash

This tool emulates UNIX terminal.
1. Download [Git for Windows](https://gitforwindows.org).
2. Install using default options, except for one step
    - In step  "Choosing the default editor for Git" select "Use Notepad++ as default Git's editor"

#### Python

1. Install Python via [Python download site](https://www.python.org/downloads/).
    - **Double check that Python is added to the PATH environmental variable**

#### Python libraries
1. Install dependencies located in `requirements.txt` using following command in GitBash: `pip3 install -r requirements.txt`

### Linux, Mac OS

#### Python
1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
1. MacOS
    `brew install python3`
    
    *Note:* if you do not have `brew`, install it using [this](https://brew.sh/) tutorial.

#### Python libraries

`pip3 install -r requirements.txt`

#### Text editor
You can use [Atom](https://atom.io), [Sublime Text](http://www.sublimetext.com) or other text editor of your choice.

## Testing installation

1. Clone this repository `git clone git@github.com:anastazie/dash-pycon-2018.git` or `git clone https://github.com/anastazie/dash-pycon-2018.git`
1. In your terminal:
    ```
    cd programming-fundamentals
    python3 app.py
    ```
If you are able to see running application it means that installation was successful :)
