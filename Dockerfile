# Utiliser une base Ubuntu stable
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Correction : Forcer l'utilisation d'un miroir de secours et nettoyer les listes
RUN sed -i 's/archive.ubuntu.com/mirror.init7.net/g' /etc/apt/sources.list && \
    apt-get clean && \
    apt-get update --fix-missing && \
    apt-get install -y \
    python3-pip \
    python3-dev \
    cmake \
    libboost-all-dev \
    libeigen3-dev \
    libopenmpi-dev \
    openmpi-bin \
    libvtk7-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installation des packages Python
RUN pip3 install --no-cache-dir numpy scipy matplotlib pandas vtk mpi4py pybind11

# Récupération du code source
WORKDIR /app
# Récupération du code source ET de tous les sous-modules nécessaires
RUN git clone --recursive https://github.com/Plant-Root-Soil-Interactions-Modelling/CPlantBox.git .

# Compilation (si nécessaire pour les modules C++)
RUN cmake . && make install

# On se place dans le dossier de l'exemple pour que les chemins relatifs ../../ fonctionnent
WORKDIR /app/tutorial/examples

# Commande pour lancer l'exemple
CMD ["python3", "example1a_small.py"]