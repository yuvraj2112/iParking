# iParking
A repo that emulates an automated car-parking scenario. Written in Python.

### What to install
Before we can open for business, you need to install the below in your system.
* Download the latest version of python here: https://www.python.org/downloads/
* Download and install git here: https://git-scm.com/downloads

### Steps to run:

1. Clone git repository - git clone https://github.com/yuvraj2112/iParking.git
2. In your terminal, point to the newly cloned folder: `cd iParking`
3. At this point you need to check if you have python3 as default. For that, type: `python --version`.
4. If, in the above step you get Python 2.x, you need to first follow the section below. Otherwise, continue.
5. Let's install all the libraries we might require: `pip install -r requirements.txt`
6. If you have any command files at this point, add them to the data folder.
7. Remember the name of the command file you want to run and type: `python iParking.py data/<file_name>.txt`
8. If you want to run the test cases added: `python test.py`


#### What to do if I have both python 3 and 2 installed. Glad you asked!
1. python3 -m venv env
2. source env/bin/activate
3. You may now continue your adventure from step 5.
