

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deekoo_auth",
    version="0.0.1",
    author="Miika Mäkelä",
    author_email="makelanmiika@gmail.com",
    description="package for ocr detection",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[        
        'flask',
        'Flask-SQLAlchemy',  
        'Flask-HTTPAuth',    
        'passlib',
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    },
    entry_points={
        "console_scripts": [
            "run_server = deekoo_auth.app:run",            
        ],
    },
)
  

