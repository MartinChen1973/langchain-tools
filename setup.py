import sys
import shutil
import os
import glob
from setuptools import setup, find_packages
from subprocess import call

def read_and_increment_version():
    main_version = '0.1'
    version_file = 'last_version.txt'
    if os.path.exists(version_file):
        with open(version_file, 'r') as file:
            last_version = file.read().strip()
        if last_version.startswith(main_version):
            version_parts = last_version.split('.')
            # Increment the minor version
            version_parts[-1] = str(int(version_parts[-1]) + 1)
            new_version = '.'.join(version_parts)
        else:
            # Reset to the main version with a new minor increment
            new_version = main_version + '.0'
    else:
        # Initialize version if file does not exist
        new_version = main_version + '.0'
    
    # Write the new version back to the file
    with open(version_file, 'w') as file:
        file.write(new_version)
    
    return new_version

def remove_build_dirs():
    directories = ['dist', 'build', '*.egg-info']
    for directory in directories:
        if os.path.isdir(directory):
            shutil.rmtree(directory)
        elif glob.glob(directory):
            for dir in glob.glob(directory):
                shutil.rmtree(dir)

def setup_package():
    new_version = read_and_increment_version()
    setup(
        name='langchain-tools',
        version=new_version,
        author='Langchain Tools Team',
        author_email='cheny@cheny.com',
        description='Simplifying, enhancing, and extending the LangChain library functionality',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/MartinChen1973/langchain-tools',
        packages=find_packages(),
        install_requires=[
            'langchain', 
            'langchain-community', 
            'langchain-openai'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10'
        ],
        python_requires='>=3.7',
        keywords='language processing, AI, natural language understanding, LangChain, LLM'
    )

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Default to building the package if no arguments are provided
        sys.argv.append('sdist')
        sys.argv.append('bdist_wheel')
    
    remove_build_dirs()  # Clean old build files
    setup_package()  # Setup package

    # Call the batch file to upload to PyPI
    call(['upload.bat'], shell=True)
