Building on windows OS
----------------------
- Install python 3.7.4 (or newer)
  - visit https://python.org and download and install python 3.7

- Install pyqt5 and pyinstaller (change paths as needed for your system)
  - cd c:\folder\where\python\is\installed\Scripts
  - pip3 install PyQt5
  - pip3 install PyInstaller

- Install git
  - visit https://git-scm.com/download/win

- Download ac7parser
  - git clone https://github.com/shimpe/ac7parser

- Install ac7parser (be sure to invoke python v3)
  - cd ac7parser
  - python setup.py install

- Clone ac7renamer
  - git clone https://github.com/shimpe/ac7renamer

- Try if ac7renamer runs correctly from python source code:
  - cd ac7renamer
  - python ReStyle.py

- If that went well, you can now optionally proceed to make a standalone executable:
  - mkdir pyinstaller
  - cd pyinstaller
  - c:\folder\where\python\is\installed\Scripts\pyinstaller ..\ReStyle.py -F

At the end of the process, a "dist" folder should have appeared which contains ReStyle.exe.

Building on Linux OS
--------------------
- Prerequisites:
  -Install python 3.7
  - Install PyQt5 and PyInstaller (either using pip or using your distribution's package manager)
  - Install git

- Download ac7parser
  - git clone https://github.com/shimpe/ac7parser

- Install ac7parser (be sure to invoke python v3)
  - cd ac7parser
  - python setup.py install

- Clone ac7renamer
  - git clone https://github.com/shimpe/ac7renamer

- Try if ac7renamer runs correctly from python source code:
  - cd ac7renamer
  - python ReStyle.py

If that went well, you can now optionally proceed to make a standalone executable:
  - mkdir pyinstaller
  - cd pyinstaller
  - /folder/where/python/is/installed/Scripts/pyinstaller ../ReStyle.py -F

At the end of the process, a "dist" folder should have appeared which contains ReStyle.exe.

Building on Mac OS:
-------------------
Sorry I don't have access to a Mac OS system. If you manage to build a standalone build, 
be sure to file a pull request containing build instructions.
