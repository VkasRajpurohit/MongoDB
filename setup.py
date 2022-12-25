from setuptools import find_packages, setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "MongoDB"
VERSION = "0.0.1"
AUTHOR = "Vkas Rajpurohit"
EMAIL = "vkas.rajpurohit5226@gmail.com"
DESCRIPTION = "This is a sample project for MongoDB connection and database operations"
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirements mention in requirements.txt file
    return: This function will return a list, which contain name of libraries mentioned in requirements.txt file
    """
    try:
        with open(REQUIREMENT_FILE_NAME) as requirement_file:
            requirement_list = requirement_file.readlines()
            requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
            if HYPHEN_E_DOT in requirement_list:
                requirement_list.remove(HYPHEN_E_DOT)
            return requirement_list
    except Exception as e:
        print('Error: ', str(e))


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
