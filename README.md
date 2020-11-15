# Visual transposons

This is a WIP for a web dashboard to show _A. thaliana_ transposable elements metadata.

## Set up the working directory (Linux)

I am using `pip` and `venv` to create a virtual environment and manage the dependencies.


- Clone the repo from GitHub: 

Using HTTPS:
```buildoutcfg
git clone -b master https://github.com/bertagallegoprm/visual_transposons.git
```
Or SSH:
```
git clone -b master git@github.com/bertagallegoprm/visual_transposons.git
```
> Add remote branches if required `git checkout -b branch-name origin/branch-name`

You will need to have installed `pip` and `venv` to create the virtual environment:

- Install pip (if required):
```buildoutcfg
sudo apt install python3-pip
```

- Install venv (if required):
```buildoutcfg
sudo apt-get install python3-venv
```
- Create the environment
```
python3 -m venv env
```

- Activate the virtual environment in the working directory:
```
source env/bin/activate
```

- And install the packages from `requirements.txt`:

```buildoutcfg
pip install -r requirements.txt
```

## Run

To run python files in the environment:

```
python3 your-python-file.py 
```

See `data` for specific instructions on how to download the data and load it into a custom database.
