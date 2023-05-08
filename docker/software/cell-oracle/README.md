# Cell Oracle

[Cell Oracle](https://morris-lab.github.io/CellOracle.documentation/installation/index.html) is a software for inference and perturbation analysis of gene regulatory networks.

It has an official docker image, but here we create our own to have better control over what is installed and how (e.g. if we need to add extra dependencies in the future). Furthermore, this allows us to easily customize the underlying jupyter notebook (e.g. disable authentication, since we're running `authelia` and isolate tools using `nginx` proxy).

The container is very bare bones: it runs as `root` and is accesssible through a basic jupyter notebook interface inside `/root/notebook`. Note that if you want to use CellOracle source code (or tutorials), you'll have to put them into `/root/notebook` manually.