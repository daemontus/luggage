# STREAM

[STREAM](https://github.com/pinellolab/STREAM) is a software for inferring pseudotime bifurcations in RNA/ATAC data.

This docker image installs the official `conda` environment for STREAM version 1.1. It then registers a jupyter notebook service
that runs on port `8000` in the `/root/notebook` folder. However, it does not automatically download
the MTLRank source code or any data. 

The container runs as root and is otherwise "as simple as possible" (e.g. just `jupter notebook` instead of `jupyter lab`, no VS code support, ...).

Note that some of the dependencies still don't quite work correctly (e.g. `matplotlib` needs to be downgraded to work, but the proper
version needs some depenencies that are yanked...). But overall the results seem mostly fine.

### Build and publish

```
docker build -t $USERNAME/software-stream .
docker push $USERNAME/software-stream
```