from setuptools import setup, find_packages

setup(
    name='delocalizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "pysubs2",
        "modify-subs",
        "subdeloc-tools",
        "python-dotenv",
        "requests"
    ],
    author='Efrain Cardenas',  
    author_email='',
    description='Subtitles delocalizer.',
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/EfronC/Delocalizer",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',

)