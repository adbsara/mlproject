from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)-> List[str]:
    ''''
    this function withh return the list of requirements
    '''
    requiremets = []
    with open("requirements.txt") as file_obj:
        requiremets = file_obj.readlines()
        requiremets=[req.replace("\n", "") for req in requiremets]

        if HYPHEN_E_DOT in requiremets:
            requiremets.remove(HYPHEN_E_DOT)

    return requiremets


setup(
name='mlproject',
version='0.0.1',
author= 'sara',
author_email ='saadin.sara@gmail.com',
packages = find_packages(),
install_requires= get_requirements("requirements.txt")

)