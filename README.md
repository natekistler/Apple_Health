# Apple_Health
Collection of Python3 code to parse and analyze apple health data

# Data Format
Data is exported from apple health in an XML format. Details on how to export from the apple health app are located here: https://www.idownloadblog.com/2015/06/10/how-to-export-import-health-data/

# Files
XMLtoCSV.py coverts the export.xml file (export file from apple health apple) to a CSV file in a directory entitled 'XMLtoCSV'

HeartRate_DayofweekViolin takes heart rate data from CSV file created from XMLtoCSV.py and creates violin plots categorized by day the day of the week.
