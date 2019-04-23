'''
Created on Apr 23, 2019

@author: PIKU
'''
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class ExeCreateCommand(install):
    """Custom install setup to help run shell commands (outside shell) before installation"""

    def run(self):
        print("I am going to execute ?")
#         subprocess.run(["pyinstaller --onefile --console main.py"])
        os.system("pyinstaller --onefile --console main.py")
        install.run(self)
        
        
setup(
    cmdclass={'install': ExeCreateCommand},
    name="MyFirstExecutble",
    version="1.0.0",
    description='Creating executble from Python',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
)
