# Visual transposons

## Getting started

### Set up the working directory (linux)

I am using `pip` and `venv` to create a virtual environment and manage the dependencies.


- Clone the repo from GitHub: 
```buildoutcfg
git clone -b master https://github.com/bertagallegoprm/visual_transposons.git
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

- Activate the virtual environment in the working directory:
```
source env/bin/activate
```

- And install the packages from `requirements.txt`:

```buildoutcfg
pip install -r requirements.txt
```

### Run

To run python files in the environment:

```
python3 your-python-file.py 
```

## Data 

The data is available at the [Arabidopsis Information Resource (TAIR) website](https://www.arabidopsis.org/download/index-auto.jsp?dir=%2Fdownload_files%2FGenes%2FTAIR10_genome_release%2FTAIR10_transposable_elements), where it appears the date of the last release. 

There are two types of data:
- `data/te_attributes.txt`. Names and attributes (family and subfamily, orientation, location in the genome).
- `data/te_sequences.txt`. Sequences.

The date of the last download can be found in `data/last_download.txt`.

- To run the code and get the data:

```
python3 get_data.py 
```
