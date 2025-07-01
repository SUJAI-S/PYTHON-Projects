School Data Cleaning with Python & Anaconda
## Aim:
This project involves cleaning a raw Excel file (school\_data\_complex.xlsx) containing student data with various problems, such as:

- Missing values
- Duplicates
- Invalid email formats
- Over-range attendance
- Improper data types like dates and times

This project is developed using Python’s Pandas library inside an Anaconda environment and generates a cleaned version of an Excel file.
## Files Used:

|**File**|**Description**|
| :- | :- |
|school\_data\_complex.xlsx|Input Excel file.|
|clean\_school\_data.py|Python code for cleaning.|
|cleaned\_school\_data.xlsx|Cleaned Excel file output|
## Cleaning Steps Performed
- Remove the duplicate rows
- Drops the rows with too many missing values
- Filling the missing values with "Unknown"
- Replacing missing email with "Not Provided"
- Convert dates to proper date and time format
- Remove attendance values over 100%
- Mark missing scores as -1
- Save a cleaned Excel file
## Possible Extensions
- Deploy via Jupyter Notebook
- Automate cleanup for multiple files

