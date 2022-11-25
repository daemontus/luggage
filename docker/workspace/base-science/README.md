# \[Docker\] Workspace (science-base)

This docker image extends the `base` image and serves as an initial docker image for scientific projects.

You can still extend this image with your own functionality, but you should find all tools necessary for a mix of software development, data science and scientific writing here.

In particular, the image starts a Jupyter lab (port 8000) and Visual Studio Code server (port 8001) in your home directory. Additionally, there is `texlive` and `jupyterlab_latex` preinstalled, so you can write LaTeX documents directly in your Jupyter lab instance.

Aside from the `WORKSPACE_USER` and `PRIVATE_KEY`/`PUBLIC_KEY`, you can also provide a `VSCODE_DATA` path where persitable Visual Studio Code configuration should be stored (otherwise you'll lose things like plugins during restarts). For Jupter lab, it is recommended that you install plugins through `pip` directly in your derived image. You can also alter Jupyter lab configuration by appending to `/etc/service/jupyter/config.py`.

What is included in this image:

 - Full installation of `texlive`;
 - Development essentials: `gcc`, `cmake`, etc.;
 - "Scientific" dev packages: `liblapack-dev`, `libopenblas-dev`, `gfortran`;
 - `python`, `python-pip`, `python3-dev`, and `python-venv`;
 - `nodejs` and `npm`;
 - `r-base` and `r-base-dev`;
 - Python packages: `mypy`, `pytest`, `pandas`, `numpy`, `setuptools`, `wheel`, 
   `networkx`, `jupyterlab` and `jupyterlab_latex`;
 - R packages: `IRkernel`;

> Note: We intentionally don't install `rust` for you, because it is recommended to install it locally for the workspace user after it is created. A global installation can be only modified by `root` (which includes things like downloading dependencies).

### Build and publish

```
docker build -t $USERNAME/workspace-base-science .
docker push $USERNAME/workspace-base-science
```