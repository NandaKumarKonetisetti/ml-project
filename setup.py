from setuptools import setup,find_packages
from typing import List


HYPHEN_E_DOT = "-e ."

def get_requirements(path:str) ->List[str]:

    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements






setup(
name="student prediction project",
version="0.0.1",
author="nanda",
author_email="nandakumaroye@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)