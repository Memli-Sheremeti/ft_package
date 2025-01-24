# Creating and Publishing a Python Package

This README provides step-by-step instructions for creating, testing, and publishing a Python package.

---

## 1. Setting Up the Project Structure

Organize your project with the following structure:

```
my_package/
├── my_package/          # Package directory
│   ├── __init__.py      # Makes this directory a package
│   └── module.py        # Contains your package code
├── setup.py             # Metadata and setup configuration
├── LICENSE              # License file
├── README.md            # Project description
```

### Example Content

#### **`my_package/__init__.py`**
```python
from .module import hello_world
```

#### **`my_package/module.py`**
```python
def hello_world():
    return "Hello, world!"
```

#### **`setup.py`**
```python
from setuptools import setup, find_packages

setup(
    name="my_package",  # Package name
    version="0.0.1",  # Initial version
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
```

#### **`LICENSE`**
Add a license file (e.g., MIT license):
```plaintext
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge...
```

#### **`README.md`**
```markdown
# My Package

A simple Python package example.

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package import hello_world

print(hello_world())
```
```

---

## 2. Building the Package

1. Install the required tools:
   ```bash
   pip install setuptools wheel
   ```

2. Build the package:
   ```bash
   python setup.py sdist bdist_wheel
   ```

This will create a `dist/` directory containing files like:
```
dist/
├── my_package-0.0.1.tar.gz
└── my_package-0.0.1-py3-none-any.whl
```

---

## 3. Testing the Package Locally

1. Install the package locally:
   ```bash
   pip install ./dist/my_package-0.0.1.tar.gz
   ```

2. Test the package in a Python script:
   ```python
   from my_package import hello_world

   print(hello_world())
   ```

---

## 4. Publishing to PyPI

1. Install `twine`:
   ```bash
   pip install twine
   ```

2. Upload to Test PyPI (optional):
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

3. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

---

## 5. Installing from PyPI

After publishing, the package can be installed with:
```bash
pip install my_package
```

---

## 6. Updating the Package

1. Make changes to your code.
2. Update the version in `setup.py`:
   ```python
   version="0.0.2"
   ```
3. Rebuild and upload:
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

---

## 7. Useful Commands

### Clean Previous Builds
```bash
rm -rf build dist *.egg-info
```

### Verify Metadata
```bash
pip show -v my_package
```

### Uninstall the Package
```bash
pip uninstall my_package
```