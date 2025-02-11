![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Proxmox](https://img.shields.io/badge/proxmox-proxmox?style=for-the-badge&logo=proxmox&logoColor=%23E57000&labelColor=%232b2a33&color=%232b2a33)![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
# FileServer - Flask & Proxmox

## Overview
FileServer is a lightweight file server built with Flask, designed to run on a Proxmox virtual machine. This server allows file management via a web interface and relies on Python and MySQL for backend operations.

## Proxmox Server Credentials
To access the Proxmox server, use the following credentials:
- **Username:** `root`
- **Password:** `1488Aa`

## Prerequisites
Before running FileServer, ensure you have the following installed:
- Python
- pip 
- Proxmox VM set up
- MySQL Server

## Required Python Libraries
Make sure you have these libraries installed:
```sh
pip install flask mysql-connector-python werkzeug
```

## Installation & Setup

1. Clone or transfer the `FileServer` directory to your Proxmox VM.
2. Navigate to the project directory:
   ```sh
   cd FileServer
   ```
3. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```
4. Run the server:
   ```sh
   python3 app.py
   ```

## Running the FileServer
Once the server is running, access it via your browser at:
```
http://172.20.128.28:5000
```
Ensure that the necessary firewall rules are set to allow connections to the specified port.
Must be connected to school network Akademiet-Heltberg for the website to function.

## License
This project is free to use, please copy it as you need :)

##
[User Guide](index.md)
Here is the user guide after the installation 
