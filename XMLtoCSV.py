#Import required packages
import xml.etree.ElementTree as ET
import csv

def XML_Parser(XML_File):
    #Parse XML file using ElementTree
    tree = ET.parse(XML_File)
    root = tree.getroot()

    #Open blank csv file to write data to
    with open('XMLtoCSV/health_data.csv', 'w', newline='') as health_data:
        csvwriter = csv.writer(health_data)

        health_data_head = []

        count = 0

        try:
            #Find loop over all records in xml file
            for record in root.findall('Record'):
                row = []

                #Create header columns for first row
                if count == 0:
                    health_data_head.append('type')
                    health_data_head.append('source_name')
                    health_data_head.append('source_version')
                    health_data_head.append('creation_date')
                    health_data_head.append('start_date')
                    health_data_head.append('end_date')
                    health_data_head.append('value')

                    csvwriter.writerow(health_data_head)
                    count += 1

                #Collect all records for fields needed and append to blank row
                row.append(record.attrib['type'])
                row.append(record.attrib['sourceName'])
                row.append(record.attrib['sourceVersion'])
                row.append(record.attrib['creationDate'])
                row.append(record.attrib['startDate'])
                row.append(record.attrib['endDate'])
                row.append(record.attrib['value'])

                #Write to row
                csvwriter.writerow(row)

        #Once all fields are collected and error is thrown for incorrect key, this catches that error
        except KeyError:
            print('Done')

        #Close the file
        finally:
            health_data.close()

#Call function with correct file name (file must be in folder)
XML_Parser('export.xml')