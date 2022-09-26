FROM jupyter/base-notebook:python-3.10.6

COPY docker/jupyter_notebook_config.py /home/${NB_USER}/.jupyter/jupyter_notebook_config.py

ENV JUPYTER_TOKEN="<generated>";

COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN mamba install --yes --file /tmp/requirements.txt && \
    mamba clean --all -f -y

USER root

RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY docker/entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

USER ${NB_USER}

ENTRYPOINT ["/usr/local/bin/entrypoint"]
CMD ["/usr/local/bin/start-notebook.sh"]
