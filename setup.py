from setuptools import setup, find_namespace_packages


setup(
    name="airathon",
    version="0.1.0",
    description="Competiton of Deep Learning, Spring 2022, Columbia University",
    author="Zehua Chen, Hongshuo Yang",
    author_email="zc2616@columbia.edu, hy2712@columbia.edu",
    packages=find_namespace_packages(include=["airathon.*"]),
    entry_points={
        "console_scripts": [
            "airathon=airathon.cli:main"
        ],
    },
)
