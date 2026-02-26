import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

url = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2042509&reg=3&lang=2"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Website accessed successfully")
else:
    print("Error:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")
print("Total tables found:", len(tables))

df_raw = pd.read_html(StringIO(str(tables[2])))[0]

print("Raw Data:")
print(df_raw.head())
print(df_raw.to_string())

df_raw.to_csv("raw_data.csv", index=False)
print("Raw data saved successfully.")

df = df_raw.copy() #to create a copy of raw data to clean and analyze

#to remove the first garbage data row containing repeated titles 
#start taking second rows onwards
df = df.iloc[1:] 
df.columns = df.iloc[0] # Set second row as column names
df = df.iloc[1:] # Remove that header row (row 0) from data that we used as column names

df = df[df["States/UTs"] != "Total (All India)"] #to remove last row that gives Total 
df.drop(columns=["S. No."], inplace=True) #to drop serial number column

df.rename(columns={"States/UTs": "State"}, inplace=True) #to rename column name (States/UTs) to (State)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce") #to convert year type to numeric

#to replace empty cells with median ,as accident can have very high numbers
for col in df.columns[1:]:
    df[col] = df[col].fillna(df[col].median())

df.reset_index(drop=True, inplace=True) #reset index from (1,2,3...) to (0,1,2,...)
print("\nCleaned Data")
print(df.to_string())
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved successfully.")

#Simple Visualisation
total_accidents_per_year = df.iloc[:, 1:].sum()
plt.figure()
plt.bar(total_accidents_per_year.index, total_accidents_per_year.values)
plt.title("Total Road Accidents in India (2018-2022)")
plt.xlabel("Year")
plt.ylabel("Total Accidents")
plt.show()

top5 = df.sort_values("2022", ascending=False).head(5) #sort in descending order the column 2022
print("\nTop 5 states")
print(top5)
plt.figure()
plt.bar(top5["State"], top5["2022"])
plt.title("Top 5 States by Accidents in 2022")
plt.xlabel("State")
plt.ylabel("Accidents in 2022")
plt.xticks(rotation=45) #to rotate names and avoid overlapping
plt.show()