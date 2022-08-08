from setuptools import setup, find_packages

setup(
    name="pythonic-spring",
    version="0.0.1.2",
    description="A python-made framework like Spring in Java.",
    author="Tianhao Zhang",
    author_email="genji9071@gmail.com",
    license="MIT",
    keywords="spring pythonic",
    project_urls={
        "Source": "https://github.com/genji9071/pythonic-spring/",
        "Tracker": "https://github.com/genji9071/pythonic-spring/issues"
    },
    packages=find_packages(),
    install_requires=["pydantic==1.8.2"],
    python_requires=">=3"
)