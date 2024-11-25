# \[Docker\] Workspace (base-conda)

A very simple "base" image that includes R, Python and `conda` package manager (`pip` and `venv` are still available).

As opposed to `base-science`, this package does not provide any "advanced" functionality such as Jupyter notebooks and VS Code server. However, thanks to this it remains "reasonably small" at 1.3GB. 

Due to the missing Jupyter/VS Code, it is not really suitable for remote work, but it can be used as a basis for something like a reproducibility package.

### Build and publish

```
docker build -t $USERNAME/workspace-base-conda .
docker push $USERNAME/workspace-base-conda
```