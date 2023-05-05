# MTLRank

[MTLRank](https://github.com/alexQiSong/MTLRank) is a software for inferring gene regulatory networks from single cell RNA/ATAC data.

This docker image installs the official `conda` environment for MTLRank version 1.0. It then registers a jupyter notebook service
that runs on port `8000` in the `/root/notebook` folder using the `MTLRank` environment. However, it does not automatically download
the MTLRank source code or any data.

Furthermore, note that MTLRank needs quite a bit of data, so make sure to mount `/root/notebook` to some outside location with
sufficient storage capacity. 

The container runs as root and is otherwise "as simple as possible" (e.g. just `jupter notebook` instead of `jupyter lab`, no VS code support, ...).

In terminal, use `conda activate MTLRank` to activate the `MTLRank` environment. Also, note that due to the "minimal" setup, the
default working directory in the terminal is not `/root/notebook`! You have to run `cd /root/notebook` before downloading new data.