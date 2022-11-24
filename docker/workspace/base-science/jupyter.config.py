# Configuration file for lab.

c = get_config()  # noqa

## The IP address the Jupyter server will listen on.
#  Default: 'localhost'
c.ServerApp.ip = '0.0.0.0'

## Whether to open in a browser after starting.
#                          The specific browser used is platform dependent and
#                          determined by the python standard library `webbrowser`
#                          module, unless it is overridden using the --browser
#                          (ServerApp.browser) configuration option.
#  Default: False
c.ServerApp.open_browser = False

## The port the server will listen on (env: JUPYTER_PORT).
#  Default: 0
c.ServerApp.port = 8000

## The directory to use for notebooks and kernels.
#  Default: ''
#c.ServerApp.root_dir = '~/'

## DEPRECATED, use root_dir.
#  Default: ''
#c.ServerApp.notebook_dir = '~/'

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
c.ServerApp.token = ''
