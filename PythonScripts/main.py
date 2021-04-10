

# Press the green button in the gutter to run the script.
import csv
import community_report

if __name__ == '__main__':
    mainFile = open('CountyData.csv', 'w')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["County", "State", "Mask Mandate", "Case per 100k", "Case Increase", "Death Increase",
                         "Positivity Rate"])
    community_report.main()