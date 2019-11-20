"""
DT249: Programming & Algorithms 1, Assignment

By: Karl Finnerty
"""


def get_stuff_from_net(url):
    """
    Author of function: Mark Foley
    This function accepts a URL as input and attempts to retrieve this resource from the Net.
    :param url: The required resource URL, fully qualified, i.e. http{s}://... Add a space at the end or else you'll
    attempt to launch a browser
    :return: The content of the resource appropriately decoded if possible.
    """
    try:
        import requests

        response = requests.get(url)
        print("-" * 50)
        for k, v in response.headers.items():
            print(f"{k}: {v}")
        print(f"Status code: {response.status_code} - {response.reason}")
        print(f"Encoding: {response.encoding}")
        print("-" * 50)

        if response.status_code > 399:
            raise ValueError(f"HTTP status code is {response.status_code} - {response.reason}. ")
        if response.encoding:
            return response.content.decode(response.encoding)
        return response.content.decode()
    except Exception as e:
        print(f"Something bad happened when trying to get {url}.\nI can't return anything.\n{e}")
        return None


# (1) Download the Google share price data for the net and put it into a .csv file
container_csv_text = get_stuff_from_net("http://193.1.33.31:88/pa1/GOOGL.csv")

csv_text = container_csv_text.strip()  # strips whitespace from the end of the text

# (2) Create a list in which each element will be a string i.e. a line of text from the .csv file
csv_rows = csv_text.split('\n')

# 3. Create a list of lists. The elements of (2) separated by the comma in the string
csv_rows_lists = []

for string in csv_rows:
    csv_rows_lists.append(string.split(','))

    # 3.1. This creates a new google_parsed.csv file of the contents that are in the data list.
    # Note this is not used in the program, it is just for future reference
with open('google_sp_parsed.csv', 'w') as g:
    g.write('YEAR' + ',' + 'MONTH' + ',' + 'ADJ. CLOSE' + ',' + 'VOLUME\n')
    for row in csv_rows_lists[1:]:
        g.write(row[0][:4] + ',' + row[0][:4] + row[0][5:7] + ',' + row[5] + ',' + row[6] + '\n')

# # 4. Make a final list whose elements will be the data we need i.e. 'Year', 'Month', 'Adj. Close', 'Volume'
data = []

for row in csv_rows_lists[1:]:
    yr = row[0][:4]
    mth = row[0][:4] + row[0][5:7]
    price = float(row[5])
    vol = int(row[6])
    data.append([yr, mth, price, vol])

# 5. Make dictionary of the average Adj. Close Price for each year
run_vol_yr = 0
run_close_by_vol_yr = 0
avg_price_yr = 0
avg_price_yr_dict = {}

for row in data:
    if row[0] not in avg_price_yr_dict:
        run_vol_yr = row[3]
        run_close_by_vol_yr = row[2] * row[3]
        avg_price_yr = run_close_by_vol_yr / run_vol_yr
        avg_price_yr_dict[row[0]] = avg_price_yr
    else:
        run_vol_yr += row[3]
        run_close_by_vol_yr += row[2] * row[3]
        avg_price_yr = run_close_by_vol_yr / run_vol_yr
        avg_price_yr_dict[row[0]] = avg_price_yr

# 5.1. Make a list of lists of each key-value pair in avg_price_yr_dict
avg_price_yr_list = []
for k, v in avg_price_yr_dict.items():
    avg_price_yr_list.append([v, k])

# 5.2. Sort the list by the Share Prices in ascending order
avg_price_yr_list.sort()

# 5.3. Print out the required output of the Monthly Share Prices
print("Average Adj. Close - Worst 6 Years")
print("------------------------------------")
for year in avg_price_yr_list[:6]:
    print(f"{year[1]}: {year[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Years")
print("------------------------------------")
for year in avg_price_yr_list[-1:-7:-1]:
    print(f"{year[1]}: {year[0]:<.2f}")

# 6. Make dictionary of the average Adj. Close Price for each month
run_vol_mth = 0
run_close_by_vol_mth = 0
avg_price_mth = 0
avg_price_mth_dict = {}
for row in data:
    if row[1] not in avg_price_mth_dict:
        run_vol_mth = row[3]
        run_close_by_vol_mth = row[2] * row[3]
        avg_price_mth = run_close_by_vol_mth / run_vol_mth
        avg_price_mth_dict[row[1]] = avg_price_yr
    else:
        run_vol_mth += row[3]
        run_close_by_vol_mth += row[2] * row[3]
        avg_price_mth = run_close_by_vol_mth / run_vol_mth
        avg_price_mth_dict[row[1]] = avg_price_mth

# 6.1. Make a list of lists of each key-value pair in avg_price_mth_dict
avg_price_mth_list = []
for k, v in avg_price_mth_dict.items():
    avg_price_mth_list.append([v, k])

# 6.2. Sort the list by the Share Prices in ascending order
avg_price_mth_list.sort()

# 6.3. Print out the required output of the Yearly Share Prices
print("\nAverage Adj. Close - Worst 6 Months")
print("------------------------------------")
for month in avg_price_mth_list[:6]:
    print(f"{month[1][4:] + '-' + month[1][:4]}: {month[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Months")
print("------------------------------------")
for month in avg_price_mth_list[-1:-7:-1]:
    print(f"{month[1][4:] + '-' + month[1][:4]}: {month[0]:<.2f}")
