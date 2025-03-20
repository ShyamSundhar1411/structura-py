
#  **Structura**
**Automated Folder Structure & Dependency Management for Python Projects**

---

## **Overview**
Structura is a powerful **project scaffolding tool** designed to automate the creation of consistent and standardized folder structures for **Python projects**. It supports multiple frameworks and architectures, making it easy to initialize production-ready projects with just a few commands.

Whether you're building a **Flask** or **FastAPI** project, Structura handles:
- **Folder structuring**
- **Dependency installation**
- **Environment setup**
- **Custom configurations** via YAML

---

## **Features**
- **Multiple Architectures**: MVC, MVCS, Hexagonal, and more
- **Auto-Generates Folders & Boilerplate Files**
- **Dependency Management**: Supports `venv`, `pipenv`, and `poetry`
- **YAML Configuration** for flexible project initialization
- **Extensible**: Easily customize folder structures and dependencies
- **Cross-Platform Compatibility**: Works on Windows, Linux, and macOS

---

##  **Installation**

You can install Structura using `pip`:
```bash
pip install structura-py
```


---

## **Usage**

###  **Initialize a New Project**
Create a new Python project with the desired architecture:
```bash
structura init myproject --framework flask
```
For FastAPI:
```bash
structura init myproject --framework fastapi
```

### **Generate Project Files**
If you already have a project, you can simply generate the structure:
```bash
structura init
```

---

## **Folder Structure Example**

When you run `structura-py init`, it generates the following folder structure based on the chosen architecture (e.g., MVC):

```plaintext
/myproject
├── app
│   ├── __init__.py
│   ├── models
│   │   └── user.py
│   ├── services
│   │   └── user_service.py
│   ├── controllers
│   │   └── user_controller.py
│   ├── routes
│   │   └── user_routes.py
├── config
│   ├── settings.py
│   └── config.yaml
├── tests
│   ├── test_user.py
├── requirements.txt
├── .env
├── README.md
└── main.py
```
**Architecture Variations:**
- `MVC`: `models`, `services`, `controllers`, `routes`
- `MVCS`: Adds `services` layer for business logic separation
- `Hexagonal`: Adds `adapters` and `ports` folders for dependency inversion

---


## **Contributing**
We welcome contributions!
To contribute:
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Open a Pull Request (PR)

---

## **License**
Structura is licensed under the **MIT License**.
Feel free to use, modify, and distribute it.

---

##  **Feedback & Issues**
If you encounter any issues or have suggestions, feel free to open an issue on [GitHub](https://github.com/ShyamSundhar1411/structura-py/issues).

---
