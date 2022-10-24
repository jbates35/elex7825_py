# ELEX7825 Lab Project
## Robotics Class

This repo is dedicated to recreating this traditionally C++ project in Python.

### Getting started

**Warning:** There are some fairly expansive python packages that are involved in making this project run. Meaning, you may want to use a virtual environment (venv) to install the necessary dependencies to get this project going off the ground. Doing so will reduce the chance of conflicts with your Python intepreter.

To get off the ground easily, you can use Pycharm. [Download here](https://www.jetbrains.com/pycharm/download/?source=google&medium=cpc&campaign=14127625109&term=pycharm&gclid=CjwKCAjwzNOaBhAcEiwAD7Tb6JqPqNrwgy7yFO-BIpM8fSL1DFGU2z9jYmhT7CukPeDBStthFBAjBhoCJ9UQAvD_BwE#section=windows).

I used [VSCode](https://code.visualstudio.com/). If you do so, make sure you get the Python extension installed. You will also want to install a [Python (3.8 or higher) interpreter](https://www.python.org/downloads/).

**Instructions for VSCode, once you have an interpreter.**

Windows-only instructions (Hit me up if you'd like Linux or Mac instructions - mostly the same)

- Open terminal window: View -> Terminal

Optional (but recommended): [Setting up venv](https://realpython.com/python-virtual-environments-a-primer)

- Make directory in which you want the virtual environment
```
mkdir C:\venv\cv\
cd C:\venv\cv\
```
- Initiate virtual environment
```
python -m venv .
cd Scripts
.\activate
```
Note that the venv command may take a minute.

Now you can feel free to install the necessary python libraries.
```
python -m pip install numpy
python -m pip install opencv-contrib-python
python -m pip install cvui
python -m pip install Pillow
python -m pip install -U matplotlib
```
After you are done, and you've cloned this repo, [you'll want to let VSCode know where to look for the interpreter](https://code.visualstudio.com/docs/python/environments).

Essentially:
- Open command palette: View -> Command Palette...
- Type ">Python: Select Interpreter"
- Hit "Enter interpreter path..." in the dropdown menu
- You'll want to select the "python.exe" file, i.e. in this example it'd be in "C:\venv\cv\Scripts\python.exe"

I beliiievve that's it. Enjoy!
