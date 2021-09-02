FROM gitpod/workspace-full

RUN sudo apt update && \
    sudo apt dist-upgrade -y && \
    sudo apt install python3-dev python-is-python3 python3-pip neofetch -y && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    

RUN echo "export PATH='$PATH:$HOME/.poetry/bin'" >> ~/.bashrc
