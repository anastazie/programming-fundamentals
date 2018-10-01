## Installation

*Note:* Python 3.6 or higher can be used for this workshop.

### Windows

#### 1. Text editor
You can use [Notepad++](https://notepad-plus-plus.org/download/v7.5.8.html) or other text editor of your choice.

#### 2. GitBash

This tool emulates UNIX terminal.
1. Download [Git for Windows](https://gitforwindows.org).
2. Install using default options, except for one step
    - In step  "Choosing the default editor for Git" select "Use Notepad++ as default Git's editor" or other text editor that you installed

#### 3. Python

1. Install Python via [Python download site](https://www.python.org/downloads/).
    - **Double check that Python is added to the PATH environmental variable**
    - In case if you forgot to do that check out [this tutorial](https://anthonydebarros.com/2018/06/21/setting-up-python-in-windows-10/).

#### 4. Python libraries
1. Clone this repository using one of the following command in your terminal `git clone git@github.com:anastazie/programming-fundamentals.git` or `git clone https://github.com/anastazie/programming-fundamentals.git`

1. Install dependencies located in `requirements.txt` using following command in GitBash: `pip3 install -r requirements.txt`

### Linux, Mac OS

#### 1. Text editor
You can use [Atom](https://atom.io), [Sublime Text](http://www.sublimetext.com) or other text editor of your choice.

#### 2.Python
1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
1. MacOS
    `brew install python3`
    
    *Note:* if you do not have `brew`, install it using [this](https://brew.sh/) tutorial.

#### 3. Python libraries

1. Clone this repository using one of the following command in your terminal `git clone git@github.com:anastazie/programming-fundamentals.git` or `git clone https://github.com/anastazie/programming-fundamentals.git`
2. Use following command in your terminal: `pip3 install -r requirements.txt`



## Testing installation

1. In your terminal use following commands:
    ```
    cd programming-fundamentals
    python3 app.py
    ```
If you are able to see running application it means that installation was successful :)
