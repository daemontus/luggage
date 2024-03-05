# Mystery shack GPU playground

This is a VM with Nvidia GPU passthrough so that it can be used by students if needed.

The configuration is based on the `mystery-shack-docker` VM, but it has several changes:

 - First, the root password is generic so that it can be shared with students. The actual access is protected by authelia.
 - Obviously, the GPU is added here. To see how this is done, look at the pop-os VM.
 - Remote access is through the VS Code instance that is used for management on the docker machine.
 - Docker is not really running.

 - User password us the username. Root password is the machine name.