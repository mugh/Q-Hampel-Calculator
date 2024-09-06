# Download from realease page [here](https://github.com/mugh/Q-Hampel-Calculator/releases)
Two version available, .exe version and excel-addins version


# Q/Hampel Calculator

This calculator is based on ISO 13528 Robust analysist per annex C.5.4.
It will output Robust mean (x*) using hampel estimator with finite step and Robust standard deviation (s*) using Q method.


# .exe Version

## Usage

Download from release page, unzip. Double click on qhampel.exe and wait for the result. The application need input data from data.csv file. Put your data in included data.csv.


## Data.csv format

data.csv file shall be formatted like this (no header):

    data1-1,data2-1,data3-1
    data1-2,data2-2,data3-2
    data1-3,data2-3,data3-3
    data1-n,data2-n,datai-n
    and so on

Each row representing a laboratory data and each column representing data of that laboratory, it can be as many as you need just keep expand it to the right. Data.csv shall at least contain a column of data.

Each data shall be separated by comma (,) be careful when editing data.csv using excel because the save result migh be separated using semicolon (;). 

If this the case, open the data.csv using text editor such as notepad++ then press ctrl+h find ";" replace all with ","

Decimal value shall be using point (.)


# Excel-Addins Version
## Usage
Run the setup files

## How to use :
After finish install, it will create a new tab called qhampel in your excel.
Make ready your data in a sheet, click start calc from qhampel tab, it will ask your data range and after that choose at what cell the result will output


# Legal usage
The usage of this application for non-commercial shall include credit to the author.
For commercial use please contact the author for license and removal of credit, it will replaced with your license information.


# Contact and Credit
Author name : Mughni Yumashar

Contact : mughnimail@gmail.com
