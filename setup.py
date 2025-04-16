from setuptools import setup, find_packages

setup(
    name='deepgrad',
    version='0.1.0',
    description='A lightweight and modular deep learning framework',
    author='zhuohengfeng',
    author_email='39956210@qq.com',
    url='https://github.com/zhuohengfeng/deepgrad',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
)
