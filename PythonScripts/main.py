

# Press the green button in the gutter to run the script.
import csv

if __name__ == '__main__':
    mainFile = open('CountyData.csv', 'w')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["State", "Count", "Case Increase", "Mask Mandate", "Weather"])