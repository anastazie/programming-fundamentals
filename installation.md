## Installation

*Note:* Python 3.6 or higher can be used for this course.

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
2. Check Python installation
    - In GitBash type `which python`, you should see something like this:
    `/c/Users/IEUser/AppData/Local/Programs/Python/Python37-32/python`

#### 4. Python libraries
1. Clone this repository using one of the following command in your terminal `git clone https://github.com/anastazie/programming-fundamentals.git`
1. Install several libraries separately by using following commands in the terminal: 
    ```
    pip3 install pandas
    pip install pyzmq
    ```
1. To install remaining libraries that are located in `requirements.txt` use following command in GitBash: `pip3 install -r requirements.txt`

### Linux, Mac OS

#### 1. Text editor
You can use [Atom](https://atom.io), [Sublime Text](http://www.sublimetext.com) or other text editor of your choice.

#### 2.Python
1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
1. MacOS
    `brew install python3`
    
    *Note:* if you do not have `brew`, install it using [this](https://brew.sh/) tutorial.
1. Check Python installation
    - In terminal type `which python` (or `which python3` if you have multiple python versions), you should see something like this:
    `/usr/local/bin/python3`

#### 3. Python libraries

1. Clone this repository using one of the following command in your terminal `git clone https://github.com/anastazie/programming-fundamentals.git`
1. Install several libraries separately by using following commands in the terminal: 
    ```
    pip3 install pandas
    pip install pyzmq
    ```
1. To install remaining libraries that are located in `requirements.txt` use following command in your terminal: `pip3 install -r requirements.txt`



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
1. In you browser type following address: `http://127.0.0.1:8050/`. You should see barplot.
1. Quit app by typing `Ctrl+C` in terminal. 
1. Start Jupyter Notebook by typing i terminal `jupyter notebook`. Tab will open in your default browser automatically.
1. Stop Jupyter Notebook by typing `Ctrl+C` in terminal.

