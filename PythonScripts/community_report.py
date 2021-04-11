import urllib

from bs4 import BeautifulSoup
import pandas

xls = pandas.ExcelFile("CommunityProfile.xlsx")
sheet1 = pandas.read_excel(xls, "Counties")


def main():
    first_column = sheet1.iloc[:, [0, 5, 16, 19, 20, 36]]
    print(first_column)


def get_counties():
    return sheet1.iloc[:, 0]


def get_state():
    return sheet1.iloc[:, 5]


def get_cases_per_100k():
    return sheet1.iloc[:, 16]


def case_increase():
    return sheet1.iloc[:, 19]


def death_increase():
    return sheet1.iloc[:, 20]


def infectivity_rate():
    return sheet1.iloc[:, 36]
