# Configuration file for lab.

c = get_config()  # noqa


## The IP address the Jupyter server will listen on.
#  Default: 'localhost'
c.NotebookApp.ip = '0.0.0.0'


## The port the server will listen on (env: JUPYTER_PORT).
#  Default: 0
c.NotebookApp.port = 8000


## Whether to open in a browser after starting.
#                          The specific browser used is platform dependent and
#                          determined by the python standard library `webbrowser`
#                          module, unless it is overridden using the --browser
#                          (ServerApp.browser) configuration option.
#  Default: False
c.NotebookApp.open_browser = False


## Token used for authenticating first-time connections to the server.
#  
#          The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set directly
#          with the JUPYTER_TOKEN environment variable.
#  
#          When no password is enabled,
#          the default is to generate a new, random token.
#  
#          Setting to an empty string disables authentication altogether, which
#  is NOT RECOMMENDED.
#  Default: '<generated>'
c.NotebookApp.token = ''


## The directory to use for notebooks and kernels.
#  Default: ''
c.NotebookApp.notebook_dir = '/root/notebook'

## Allow runnig as root user.
#  Default: False
c.NotebookApp.allow_root = True