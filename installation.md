## Installation

*Note:* Python 3.6 or higher can be used for this workshop.

### Windows

#### Python

1. Install Python via [`anaconda`](https://www.anaconda.com/download/).
1. Install GitBash using following command Anaconda prompt: `conda install git`

#### Python libraries
1. Install dependencies located in `requirements.txt` using following command in GitBash: `while read requirement; do conda install --yes $requirement || pip3 install $requirement; done < requirements.txt`
If this is not working try following in Anaconda Prompt:
`python -m pip install -r requirements.txt`

for more details ee [Stack Overflow discussion](https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t/)

### Linux, Mac OS

#### Python
1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
1. MacOS
    `brew install python3`
    
    *Note:* if you do not have `brew`, install it using [this](https://brew.sh/) tutorial.

#### Python libraries

`pip3 install -r requirements.txt`

## Testing installation

1. Clone this repository `git clone git@github.com:anastazie/dash-pycon-2018.git` or `git clone https://github.com/anastazie/dash-pycon-2018.git`
1. In your terminal:
    ```
    cd programming-fundamentals
    python3 app.py
    ```
If you are able to see running application it means that installation was successful :)
