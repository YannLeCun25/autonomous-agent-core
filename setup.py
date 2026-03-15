from setuptools import setup, find_packages

setup(
    name="autonomous-agent-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    author="Yann LeCun",
    description="Advanced decentralized core for autonomous AI agents with reasoning capabilities.",
    url="https://github.com/YannLeCun25/autonomous-agent-core",
)
