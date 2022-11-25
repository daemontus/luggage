# \[Docker\] Workspace (daemontus-science)

This is my personal "science workspace" docker image. Derived from `base-science`, it installs my "personal" dependencies, like `rust`, `aeon` and other tools for 
software development and systems biology. Do *not* use this image with a different main user than `daemontus` (if you want a different user, fork it).

The image generally expects that `~/projects` and `~/archive` exist and are mounted to some persistable storage, but strictly speaking, it's not mandatory.

Incomplete list of tools that should be available inside the image:

 - `z3` and `gringo` (both standalone and Python packages);
 - Python packages: `pyeda`, `maturin`;
 - R packages: `bioconductor`, `dorothea`;

### Build and publish

```
docker build -t $USERNAME/workspace-daemontus-science .
docker push $USERNAME/workspace-daemontus-science
```