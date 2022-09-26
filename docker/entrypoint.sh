#!/bin/bash

mamba install --yes --file /home/${NB_USER}/requirements.txt

tini -s -g -- $@
