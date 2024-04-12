from setuptools import setup, find_packages

setup(
    name='langchain-tools',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'langchain',  # If there's a central langchain package that includes most of the functionality
        'langchain-community',  # Assuming langchain_community is a separate package
        'langchain-openai',  # Assuming langchain_openai is a separate package
        # other dependencies as necessary
    ],
    # other metadata
)
