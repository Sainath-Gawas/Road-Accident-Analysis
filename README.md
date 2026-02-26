# Road-Accident-Analysis

Scraping, cleaning and analysing road accidents data (2018-2022)

# State-wise Road Accidents in India (2018-2022)

## Website Scraped

[Press Information Bureau (PIB)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2042509&reg=3&lang=2)

**Type of Data:** State-wise road accidents from 2018 to 2022

## Techniques Performed

### Web Scraping

1. Used **Python `requests`** to fetch the webpage.
2. Parsed the HTML using **BeautifulSoup** to locate the tables.
3. Extracted the table into a **Pandas DataFrame** using `pd.read_html`.
4. Saved the raw data as `raw_data.csv`.

### Data Cleaning

1. Removed top garbage rows (repeated titles).
2. Set proper column headers and dropped the serial number column `"S. No."`.
3. Converted numeric columns to proper `int`/`float` types using `pd.to_numeric`.
4. Replaced missing values with the **median** of the column.
5. Reset the index for a clean DataFrame.
6. Saved cleaned data as `cleaned_data.csv`.

### Data Visualization

1. **Bar Chart:** Total accidents in India per year (2018–2022).
2. **Top 5 States Chart:** States with the highest accidents in 2022.

## Observations

1. Total accidents decreased in 2020, likely due to the **COVID-19 impact**.
2. **Tamil Nadu**, **Madhya Pradesh** and **Uttar Pradesh** consistently have high accident numbers.
