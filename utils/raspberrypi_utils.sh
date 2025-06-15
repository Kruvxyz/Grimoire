#!/bin/bash

set -e

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing essential packages..."
sudo apt install -y \
    git \
    curl \
    htop \
    vim \
    libffi-dev \
    libssl-dev \
    python3-dev \
    python3 \
    python3-pip \
    docker \
    docker-compose

echo "Installing GitHub CLI..."
sudo apt install -y gh

echo "Setting up Docker Compose (latest)..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Starting Docker and enabling it on boot..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Adding user to docker group..."
sudo usermod -aG docker ${USER}
echo "You may need to log out and log in again for group changes to take effect."
