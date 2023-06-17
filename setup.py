from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

with open(os.path.join(os.path.dirname(__file__), "LICENSE"), "r") as f:
    license_text = f.read()

setup(
    name='asdTools',
    version='0.0.9',
    description='Simple tools for simple goals.',
    url='https://github.com/asd123pwj/asdTools',
    author='MWHLS',
    author_email='pan45015763@163.com',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='MWHLS library',
    packages=find_packages(include=['asdTools.Classes.*']),
    install_requires=[
        'nvidia-ml-py',
        'python-docx',
        'requests',
        'Pillow',
    ],
    python_requires='>=3.6, <4',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="LGPLv3",
    data_files=[("", ["LICENSE"])],
)
