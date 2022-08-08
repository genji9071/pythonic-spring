from setuptools import setup, find_packages

setup(
    name="pythonicspring",
    version="0.0.0.1",
    description="A python-made framework like Spring in Java.",
    author="Tianhao Zhang",
    author_email="genji9071@gmail.com",
    license="MIT",
    keywords="spring pythonic",
    project_urls={
        "Source": "https://github.com/genji9071/pythonic-spring/",
        "Tracker": "https://github.com/genji9071/pythonic-spring/issues"
    },
    packages=find_packages(exclude=["test"]),
    install_requires=["pydantic==1.8.2"],
    python_requires=">=3"
)