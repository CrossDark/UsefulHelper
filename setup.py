from setuptools import setup, find_packages


setup(
    name='UNKnownDB',
    version='1.6.5',
    author='CleaverCreator',
    author_email='liuhanbo333@icloud.com',
    packages=find_packages(),
    zip_safe=False,
    platforms=['Linux'],
    install_requires=['PyQt5'],
    python_requires='>=3.9',
    description='A new Python DB',
    long_description="""
                    A DB that human can read
                    Use Unknown Describe Language
                                    """,
    license='GIL',
    url='https://github.com/CleverCreater/UNKnownDB',
    classifiers=[],
    scripts=['./start.py']
)
