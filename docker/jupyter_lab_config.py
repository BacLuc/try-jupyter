# Configuration file for lab.

c = get_config()  # noqa

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
import os
c.ServerApp.token = os.getenv('JUPYTER_SERVER_TOKEN')
