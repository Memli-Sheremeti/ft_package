from setuptools import setup, find_packages


setup(
    name = "ft_package",
    version = "0.0.1",
    summary = "A sample test package",
    home_page = "https://github.com/Memli-Sheremeti/ft_package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author = "mshereme",
    author_email = "memli.sh.pro@gmail.com",
    licence = "MIT",
    classifiers = [],
    packages = find_packages(),
    python_requires=">=3.6"
)