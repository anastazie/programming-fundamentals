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
    - In case if you forgot to do so that check out [this tutorial](https://anthonydebarros.com/2018/06/21/setting-up-python-in-windows-10/)
    - **Click on `Disable path length limit`**

#### 4. Python libraries
1. Clone this repository using one of the following command in your terminal `git clone https://github.com/anastazie/programming-fundamentals.git`
1. Install pandas by using following command in the terminal: `pip3 install pandas`
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

1. Clone this repository using one of the following command in your terminal `git clone https://github.com/anastazie/programming-fundamentals.git`
2. Install pandas by using following command in the terminal: `pip3 install pandas`
3. Use following command in your terminal: `pip3 install -r requirements.txt`



## Testing installation

1. In your terminal use following commands:
    ```
    cd programming-fundamentals
    python app.py
    ```
    *Note: use `python3 app.py` if you have multiple python versions.*
    
    You should see similar output in your terminal
    ```
   * Serving Flask app "app" (lazy loading)
   * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
   * Debug mode: off
   * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
    ```
2. In you browser type following address: `http://127.0.0.1:8050/`. You should see barplot.

