from bs4 import BeautifulSoup
import requests
import pandas as pd

PAYSCALE_URL = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'

response = requests.get(PAYSCALE_URL)
payscale_web_page = response.text

soup = BeautifulSoup(payscale_web_page, parser='html.parser',features="lxml")

data = soup.findAll(name="tr", class_="data-table__row")

list_to_csv = [["Rank"," Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "High Meaning"]]
salaries_by_college = [row.getText() for row in data]
for row in data:
    actual = row.getText()
    actual = actual.split("Rank:")[1]
    temp_rank = int(actual.split("Major:")[0])
    actual = actual.split("Major:")[1]

    temp_major = actual.split("Degree Type:")[0]
    actual = actual.split("Degree Type:")[1]

    temp_degree = actual.split("Early Career Pay:$")[0]
    actual = actual.split("Early Career Pay:$")[1]

    temp_early = float(actual.split("Mid-Career Pay:$")[0].replace(",", ""))
    actual = actual.split("Mid-Career Pay:$")[1]

    temp_mid = float(actual.split("% High Meaning:")[0].replace(",", ""))
    temp_mean = actual.split("% High Meaning:")[1]

    list_to_csv.append([temp_rank, temp_major, temp_degree, temp_early, temp_mid, temp_mean])

for item in list_to_csv:
    print(item)

df =  pd.DataFrame(list_to_csv)

df.to_csv('salaries_updated.csv', sep=',', header=None, index=None)

##only pandas solution ------------------------------------------------------------------
# # Main dataframe to collect all data
# table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
# df = table_from_html[0].copy()
# df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
#
# # Add tables from other pages to main dataframe
# for page_no in range(2, 35):
#     table_from_html = pd.read_html(
#         f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
#     page_df = table_from_html[0].copy()
#     page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
#     df = df.append(page_df, ignore_index=True)
#
# # Select necessary columns only
# df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]
#
# # Clean columns
# df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)
#
# # Change datatype of numeric columns
# df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)