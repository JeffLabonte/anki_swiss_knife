FROM gitpod/workspace-full

USER gitpod
ENV PATH=$PATH:$HOME/.poetry/bin
ENV PIP_USER="no"

RUN sudo apt update && \
    sudo apt dist-upgrade -y && \
    sudo apt install python3-dev python-is-python3 python3-pip neofetch firefox firefox-geckodriver -y && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
