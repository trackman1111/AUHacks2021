import urllib

from bs4 import BeautifulSoup
import pandas

xls = pandas.ExcelFile("CommunityProfile.xlsx")
sheet1 = pandas.read_excel(xls, "Counties")

def main():
    first_column = sheet1.iloc[:, [0, 5, 16, 19, 20, 36]]
    print(first_column)




