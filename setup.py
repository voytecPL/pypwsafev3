import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(name='pypwsafev3',
      version='0.0.3',
      description="A pure-Python library (based on https://github.com/ronys/pypwsafe and it's forks) that can read and write Password Safe v3 files, originally by Paulson McIntyre http://pwsafe.org",
	  long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/voytecPL/pypwsafev3',
      author='Wojciech Jakubas',
      author_email='wojciech.jakubas@gmail.com',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
       ],
	   install_requires=[
		  'pycryptoplus',
		  'pycryptodome',
      ]
	)
