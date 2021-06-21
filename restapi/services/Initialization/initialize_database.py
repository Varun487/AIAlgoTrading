from pandas_datareader import data
import pandas as pd
import psycopg2

print()
print("INITIALIZING DB")

#################### SETUP DATABASE CONNECTION ####################
print()
print("----------STEP 1/5----------")
print()

print("Setting up DB connection...")

# Set up database connection
conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432,
)

# setup cursor
cur = conn.cursor()

print("Connected to DB")

#################### SETUP COMPANY TABLE IN DB ####################
print()
print("----------STEP 2/5----------")
print()

print("Adding companies data to DB...")

# get all nifty 50 companies
nifty_companies = pd.read_csv('/home/app/restapi/services/Initialization/nifty50list.csv')

# Delete all rows from company table
cur.execute('DELETE FROM strategies_Company')
conn.commit()

# iterate through all companies and insert them into database
for company in range(len(nifty_companies)):
    company_name = nifty_companies['Company Name'][company] + " NSE"
    company_ticker = nifty_companies['Symbol'][company] + ".NS"
    company_description = f"Industry: {nifty_companies['Industry'][company]} Series: {nifty_companies['Series'][company]} ISIN Code: {nifty_companies['ISIN Code'][company]}"
    cur.execute(f"INSERT INTO strategies_Company VALUES ({company+1}, '{company_name}', '{company_ticker}', '{company_description}');")
    conn.commit()

print("Completed adding companies to DB")

#################### SOURCE DATA FROM YAHOO FINANCE AND PUSH TO DB ####################
print()
print("----------STEP 3/5----------")
print()

# for ticker in range(len(nifty_companies)):
#     print(nifty_companies['Symbol'][ticker])

# Get data from Yahoo finance
# panel_data = data.DataReader('TCS.NS', 'yahoo', '2021-04-01', '2021-05-31')
# print(panel_data)
# panel_data.to_csv('../TCS_Yahoo_data.csv')

#################### CLOSE DB CONNECTION ####################
print("--------------------")

cur.close()
conn.close()

print("Closing connection to db")
print("--------------------")

print()
print("DB INITIALIZATION COMPLETE")
print()
