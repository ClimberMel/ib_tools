# Notes on parms folder

## What goes here:

* I keep parameter files in json format in this folder.  This prevents hard coding usernames, passwords etc.  I also have account parameters for various tools.

* Example file report.json

* {"rptID":"123456", "token":"11507859573166978654321", rptname":"Activity_allDataYTD_xml", "outfolder":"output/flex/"}

* I have created a parms.json file that has 2 levels connect (with all the conntion info) and account (With all the account information including alias for the accounts).

* {"A7894561" : "Advisor", "X1234678": "M-ROTH", "X9871235": "F-TFSA", "X5551237": "F-IRA", "X3322114": "M-Margin"}

* the account section will read in the available accounts, but also Alias names that are helpful on reports.  
* For example "X1234678": "M-ROTH" it may be hard to remember the account number, M-ROTH would be much easier to recognize in the reports.

file.py is used to read these json files.
dlFlexToMultiXL.py has a sample of how I call and use my report.json file

## Folder structure

* Keep the folder structure as I have it setup, then you can put parm files in the parm folder and output will be written to the output folder from any of the sample code.
