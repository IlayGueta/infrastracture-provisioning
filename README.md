# DevOps Infrastructure Automation — User Guide

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> ⚠️ **This tool runs on Linux only.**

---

## ✨ Features

- **Automated VM Provisioning** - Create virtual machines via CLI
- **Pydantic Validation** - Automatic input validation with custom exceptions
- **Configuration Management** - Persistent JSON storage for VM configs
- **Unique Identifiers** - UUID generation for every VM
- **Custom Exceptions** - Structured error handling
- **Logging System** - Complete audit trail of operations
- **Type Safety** - Full type hints with Pydantic models

---

## 🛠️ Technologies

- **Python 3.8+** - Core language
- **Pydantic 2.0+** - Data validation and settings management
- **JSON** - Configuration persistence
- **Logging** - Operation tracking
- **Bash** - Automation scripts
- **Git** - Version control

**Future Enhancements:**
- Docker containerization
- Terraform integration
- AWS deployment
- Web API (FastAPI)
- Database support (SQLite/PostgreSQL)

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/IlayGueta/infrastructure-provisioning.git
cd infrastructure-provisioning

# 2. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run

Always run from the project root directory:

```bash
python3 src/automation.py
```

---

## 💻 How to Use

The tool will prompt you to define virtual machines one by one.

#### 1. Machine Name
- Max 10 characters
- Must be unique
- Type `done` to finish and exit

#### 2. OS
Choose one of: `ubuntu`, `centos`

#### 3. CPU
Choose one of: `1vcpu`, `2vcpu`, `4vcpu`, `8vcpu`, `16vcpu`

#### 4. RAM
Choose one of: `2gb`, `4gb`, `8gb`, `16gb`, `32gb`, `64gb`

---

## 📋 Example Session

```
Welcome to Infra Automation!

Enter machine name (or 'done' to finish): web
Enter OS ['ubuntu', 'centos']: ubuntu
Enter CPU (e.g., 2vCPU): Available resources [1, 2, 4, 8, 16] vCPUs : 4vcpu
Enter RAM (e.g., 4GB): Available resources in GB [2, 4, 8, 16, 32, 64] : 8gb

Enter machine name (or 'done' to finish): done

Created machines: [{'id': '7db4308f-...', 'name': 'web', 'os': 'ubuntu', 'cpu': '4vcpu', 'ram': '8gb'}]
```

---

## ❌ Failure Examples

**Name too long (over 10 characters):**
```
Enter machine name (or 'done' to finish): verylongname

VMNameError: VM name must be 10 characters or less
```

**Empty name:**
```
Enter machine name (or 'done' to finish): (pressed Enter)

VMNameError: VM name cannot be empty
```

**Duplicate machine name:**
```
Enter machine name (or 'done' to finish): web

VMNameError: Machine name already exists
```

**Invalid OS:**
```
Enter OS ['ubuntu', 'centos']: windows

VMOSError: OS must be one of: ubuntu, centos
```

**Wrong CPU format (missing 'vcpu' suffix):**
```
Enter CPU (e.g., 2vCPU): Available resources [1, 2, 4, 8, 16] vCPUs : 4 cores

VMResourceError: CPU format must be like '4vcpu'
```

**Invalid CPU value (not in allowed list):**
```
Enter CPU (e.g., 2vCPU): Available resources [1, 2, 4, 8, 16] vCPUs : 3vcpu

VMResourceError: CPU must be one of: [1, 2, 4, 8, 16] vCPUs
```

**Wrong RAM format (missing 'gb' suffix):**
```
Enter RAM (e.g., 4GB): Available resources in GB [2, 4, 8, 16, 32, 64] : 8

VMResourceError: RAM format must be like '8gb'
```

**Invalid RAM value (not in allowed list):**
```
Enter RAM (e.g., 4GB): Available resources in GB [2, 4, 8, 16, 32, 64] : 10gb

VMResourceError: RAM must be one of: [2, 4, 8, 16, 32, 64] GB
```

---

## 📁 Output

**`configs/instances.json`** — saves every machine you create:

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

**`logs/provisioning.log`** — records every provisioning step automatically.

---

## 👨‍💻 Author

**Ilay Gueta**

- GitHub: [@IlayGueta](https://github.com/IlayGueta)
- Project: [Infrastructure Provisioning](https://github.com/IlayGueta/infrastructure-provisioning)
