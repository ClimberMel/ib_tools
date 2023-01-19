# Notes on parms folder

## What goes here:

* I keep parameter files in json format in this folder.  This prevent hard coding usernames, passwords etc.  I also have account parameters for various tools.

* Example file report.json

* {"rptID":"123456", "token":"11507859573166978654321", rptname":"Activity_allDataYTD_xml", "outfolder":"Output/flex/"}

file.py is used to read these json files.
dlFlexToMultiXL.py has a sample of how I call and use my report.json file

## Folder structure

* Keep the folder structure as I have it setup, then you can put parm files in the parm folder and output will be written to the Output folder from any of the sample code.

