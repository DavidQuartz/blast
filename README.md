# BLAST Project
The BLAST (Basic Local Alignment Search Tool) Project is a bioinformatics project focused on providing a set of tools and algorithms for biological data analysis.

## Getting Started
These instructions will guide you on how to setup the BLAST project on your local machine for development and testing purposes.

## Prerequisites
1. Python 3.7 or higher installed on your machine. You can download Python here.
2. Pip (Python package installer). Pip is included by default with Python 3.4 and later versions.
3. Virtualenv for creating an isolated Python environment. Install it using pip:

```cmd
pip install virtualenv
```

## Installation
1. First, clone the repository to your local machine:
```cmd
git clone https://github.com/DavidQuartz/blast.git
```

2. Navigate to the project directory:
```cmd
cd blast
```

3. Set up a Python virtual environment and activate it:
```cmd
python -m venv env
source env/bin/activate
```

4. Install the project dependencies:
```cmd
pip install -r requirements.txt
```

Now, you can run your Python script with the following command:
```cmd
python main.py
```

To exit venv, use the command:
```cmd
deactivate
```