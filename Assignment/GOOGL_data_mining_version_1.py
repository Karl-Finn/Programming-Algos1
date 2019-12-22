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


def average_price(a_list):
    """
    :param: a list of lists whose elements are a: date/year, adj. close price,
            volume of shares traded on that date
    :return: a dictionary of the average price for each date
    """
    avg_p_dict = {}
    for i in a_list:
        f_date = i[0]
        close = i[1]
        volume = i[2]
        if f_date not in avg_p_dict:
            run_vol = volume
            run_close_by_vol = close * volume
            avg_price = run_close_by_vol / run_vol
            avg_p_dict[f_date] = avg_price
        else:
            run_vol += volume
            run_close_by_vol += close * volume
            avg_price = run_close_by_vol / run_vol
            avg_p_dict[f_date] = avg_price
    return avg_p_dict


def dict_to_list(a_dict):
    """
    :param: a dictionary in which the values are numerical
    :return: a list in which the elements are each key-value pair of the
            dictionary, but given in [value, key] format, and sorted by value
    """
    f_list = []
    for k, v in a_dict.items():
        f_list.append([v, k])
    f_list.sort()
    return f_list


# (1) Download the Google share price data for the net and put it into a .csv file
container_csv_text = get_stuff_from_net("http://193.1.33.31:88/pa1/GOOGL.csv")

csv_text = container_csv_text.strip()  # strips whitespace from the end of the text

# (2) Create a list in which each element will be a string i.e. a line of text from the .csv file
csv_rows = csv_text.split('\n')

# 3. Create a list of lists. The elements of (2) separated by the comma in the string
csv_rows_lists = []
for string in csv_rows:
    csv_rows_lists.append(string.split(','))

# # 4. Make a final lists whose elements will be the data we need i.e. 'Date', 'Adj. Close', 'Volume'
yr_data = []
for date in csv_rows_lists[1:]:
    yr = date[0][:4]
    price = float(date[5])
    vol = int(date[6])
    yr_data.append([yr, price, vol])

mth_data = []
for date in csv_rows_lists[1:]:
    mth = date[0][:4] + date[0][5:7]
    price = float(date[5])
    vol = int(date[6])
    mth_data.append([mth, price, vol])

# 5.
yearly_prices = average_price(yr_data)
avg_price_yr_list = dict_to_list(yearly_prices)
# 5.3. Print out the required output of the Monthly Share Prices
print("Average Adj. Close - Worst 6 Years")
print("------------------------------------")
for year in avg_price_yr_list[:6]:
    print(f"{year[1]}: {year[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Years")
print("------------------------------------")
for year in avg_price_yr_list[-1:-7:-1]:
    print(f"{year[1]}: {year[0]:<.2f}")

# 6.
monthly_prices = average_price(mth_data)
avg_price_mth_list = dict_to_list(monthly_prices)
# 6.3. Print out the required output of the Yearly Share Prices
print("\nAverage Adj. Close - Worst 6 Months")
print("------------------------------------")
for month in avg_price_mth_list[:6]:
    print(f"{month[1][4:] + '-' + month[1][:4]}: {month[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Months")
print("------------------------------------")
for month in avg_price_mth_list[-1:-7:-1]:
    print(f"{month[1][4:] + '-' + month[1][:4]}: {month[0]:<.2f}")
