import os
c = get_config()  # noqa

c.NotebookApp.token = os.getenv('JUPYTER_TOKEN', '<generated>')
