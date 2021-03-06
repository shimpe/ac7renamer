from distutils.core import setup

setup(
    name='ac7renamer',
    version='0.0.1',
    packages=['ac7renamer'],
    url='https://github.com/shimpe/ac7renamer',
    license='GPLv3',
    author='shiihs',
    author_email='b13d1be5@opayq.com',
    description='Change display name of AC7 files.',
    install_requires=[ "https://github.com/shimpe/ac7parser", "PyQt5" ],
    entry_points={"console_scripts": ["realpython=ac7renamer.ac7renamer:main"]},
)
