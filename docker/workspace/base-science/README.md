# \[Docker\] Workspace (science-base)

This docker image serves as a "baseline" for users working on scientific projects. 

You are expected to create your personal workspace docker image with your own project-specific dependencies, which is then based on this image to provide the core tools.

With `luggage`, we found that most users working on scientific content do a combination of software development, data science, and scientific writing. Therefore, the `science-base` workspace image incorporates both `jupyter-lab` and `vscode-server`, and there is even a `latex` installation. From `jupyter-lab`, you can then semalessly build and preview `latex` documents.

Aside from normal requirements for base images, you should also specify `VSCODE_DATA` variable which points to a persistent storage where vscode can store its configuration.

What is included in this image:

 - Based on [phusion](https://github.com/phusion/baseimage-docker) docker images, a baseline minimal ubuntu installation.
 - Full installation of `texlive`;
 - Utilities: `git`, `htop`, `curl`, `wget`, `sudo`;
 - Development essentials: `gcc`, `cmake`, etc.;
 - "Scientific" dev packages: `liblapack-dev`, `libopenblas-dev`, `gfortran`;
 - `python`, `python-pip`, `python3-dev`, and `python-venv`;
 - `nodejs` and `npm`;
 - `r-base` and `r-base-dev`;
 - Python packages: `mypy`, `pytest`, `pandas`, `numpy`, `setuptools`, `wheel`, 
   `networkx`, `jupyterlab` and `jupyterlab_latex`;
