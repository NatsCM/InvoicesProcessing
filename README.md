# InvoicesProcessing

This tiny programm process a store invoices and extracts some needed data.

Two ways to install and launch the app (once the app folder is already in the local machine), but first thing first :

## Check if Python is already installed (This is needed cause this is a Python language based program)

* Search for "Windows Terminal" or "Command Prompt"

* Run the commandline : python --version

* If Python is installed you should see something like : Python 3.11.7

* Otherwise try this commandline : python3 --version

* If Python is installed you should see something like : Python 3.11.7

* If there is no positive answer for these two commands, run the commandline : check_and_launch.bat

* This should open the python official site

* Download the Python installer (e.g. python-3.12.2-amd64.exe) and rename it to python-installer.exe in the same folder

* Install Python and then re-run the commandline : check_and_launch.bat

* When sure that Python is installed you can run the commandline : run.bat

* A file named "mailText.txt" should appear in the folder with the extracted data

### USING THE APP WITHOUT ANY CHECK

## On the Terminal

* Search for "Windows Terminal" or "Command Prompt"
  
* Go to the program folder using the commandline : cd "folder-path"

* Run the following commandline once to install all : launch.bat

* Remember to put all the pdf invoices of the day in the folder named "receipts"

* Then use this commandline to use the app : run.bat

* A file named "mailText.txt" should appear in the folder with the extracted data

## With the .EXE file

* Get in the app folder using the windows explorer

* Double click on the file called "main"

* Now you should see a graphic interface

* Remember to put all the pdf invoices of the day in the folder named "receipts"

* Press on the botton to process the files

* A file named "mailText.txt" should appear in the folder with the extracted data
