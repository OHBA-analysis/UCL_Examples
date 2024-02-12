# UCL Example Scripts

This repository contains example scripts for analysing MEG data collected at UCL.

## Installation

To run these scripts you need to install:

- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation) (FMRIB Software Library).
- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html)).
- [OSL](https://github.com/OHBA-analysis/osl) (OHBA Software Library).
- [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics) (OSL Dynamics Toolbox) - only needed if you want to train models for dynamics.

### Windows

If you're using a Windows machine, you will need to install the above in [Ubuntu](https://ubuntu.com/wsl) using a Windows subsystem. 

Instructions:

1. Install FSL using the instructions [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/Windows). Make sure you setup XLaunch for the visualisations.

2. Install [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) inside your Ubuntu terminal:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
```

3. Install OSL and osl-dynamics:

```
curl https://raw.githubusercontent.com/OHBA-analysis/osl/main/envs/windows.yml > windows.yml
conda env create -f windows.yml
rm window.yml
```

This will create a conda environment called `osl` which contains both OSL and osl-dynamics.

### Test the installation

The following should not raise any errors:

```
conda activate osl
python
>> import osl
>> import osl_dynamics
```

### Get the latest source code (optional)

If you want the very latest code you can clone the GitHub repo. This is only neccessary if you want recent changes to the package that haven't been released yet.

First install OSL/osl-dynamics using the instructions above. Then clone the repo and install locally from source:

```
conda activate osl

git clone https://github.com/OHBA-analysis/osl.git
cd osl
pip install -e .
cd ..

git clone https://github.com/OHBA-analysis/osl-dynamics.git
cd osl-dynamics
pip install -e .
```

After you install from source, you can run the code with local changes. You can update the source code using

```
git pull
```

within the `osl` or `osl-dynamics` directory.

## Getting help

You can email chetan.gohil@psych.ox.ac.uk if you run into errors, need help or spot any typos.
