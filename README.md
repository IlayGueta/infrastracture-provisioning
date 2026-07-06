# DevOps Infrastructure Provisioning & Configuration Automation
![Python](https://img.shields.io/badge/Python-3-blue?logo=python)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?logo=git)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

A Python-based infrastructure automation project that simulates the provisioning and configuration of virtual machines.

This project is part of my DevOps learning journey and will gradually evolve into a complete infrastructure automation tool.

---

## Features

- Create virtual machines interactively
- Input validation
- Unique machine names
- UUID generated for every VM
- Save VM configuration into JSON
- Multiple VM support
- Persistent configuration storage

---

## Technologies

- Python 3
- JSON
- Git & GitHub

Future technologies:

- Pydantic
- Logging
- Bash
- Docker
- Terraform
- AWS

---

## Project Structure

```
DevopsProject-Infra-Automation
│
├── configs/
│   └── instances.json
│
├── logs/
│
├── src/
│   ├── automation.py
│   └── infra_simulator.py
│
├── .gitignore
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/IlayGueta/infrastructure-provisioning.git
```

Move into the project:

```bash
cd infrastructure-provisioning
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

---

## Running the project

Run:

```bash
python ./src/automation.py
```

---

## Example

```
Enter machine name: web

Enter OS:
ubuntu

Enter CPU:
4vcpu

Enter RAM:
8gb

Machine created successfully
```

Generated JSON:

```json
{
    "machines": [
        {
            "id": "7db4308f-4978-46d3-90fc-49bd5b4702f1",
            "name": "web",
            "os": "ubuntu",
            "cpu": "4vcpu",
            "ram": "8gb"
        }
    ]
}
```

---

## Current Progress

- Input validation
- JSON persistence
- UUID generation
- Duplicate machine name validation

---

## Roadmap

- Infrastructure simulator
- Logging
- Pydantic models
- CLI arguments
- Bash automation
- Docker support
- AWS integration
- Terraform provisioning

---

## Author

**Ilay Gueta**

GitHub:
https://github.com/IlayGueta