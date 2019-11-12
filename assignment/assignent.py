"""NOT COMPLETED"""

import csv

def get_text_file_from_net(text_url):
    """Takes a URL of a text file that is on the web as
        a string and returns the text file as a string
        using the Request Library."""
    try:
        import requests
        retrieve = requests.get(text_url)
        text_file_str = retrieve.text
        return text_file_str
    except Exception as err:
        print(f"Error trying to retrieve the file from the net: {err}")
        return None

#-----------------------------------------------------------------------------------------------------------------------
# (1) Download the Google share price data for the net and put it into a .csv file
#-----------------------------------------------------------------------------------------------------------------------
container_csv_text = get_text_file_from_net("http://193.1.33.31:88/pa1/GOOGL.csv")
csv_text = container_csv_text.strip() # strips whitespace from the end of the text

#-----------------------------------------------------------------------------------------------------------------------
# (2) Create a list in which each element will be a string i.e. a line of text from the .csv file
#-----------------------------------------------------------------------------------------------------------------------
csv_rows = csv_text.split('\n')

#-----------------------------------------------------------------------------------------------------------------------
# 3. Create a list of lists. The elements of (2) separated by the comma in the string
#-----------------------------------------------------------------------------------------------------------------------
csv_rows_lists = []
for row in csv_rows:
    csv_rows_lists.append(row.split(','))

#-----------------------------------------------------------------------------------------------------------------------
# 4. Make a final list whose elements will be the only 2 pieces of data we need i.e. 'Date' and 'Adj. Close'
#-----------------------------------------------------------------------------------------------------------------------
data = []
for row in csv_rows_lists:
    data.append([row[0], row[5], row[6]])

days_in_year = 0
vol_times_cls_yr = 0
total_volume_yr = 0
average_yr_price = 0

days_in_mth = 0
vol_times_cls_mth = 0
total_volume_mth = 0

year = int(data[1][0][0:4])
month = int(data[1][0][5:7])

row_number = 1

while row_number <= len(data):
    if data[row_number][0][0:4] == year:
        total_volume_yr += int(data[row_number][2])
        vol_times_cls_yr += float(data[row_number][1]) * int(data[row_number][2])
        average_yr_price = vol_times_cls_yr / total_volume_yr
        row_number += 1
    else:
        print(f"The average yearly price for {year} is: {average_yr_price}")
        year += 1
        total_volume_yr = 0
        vol_times_cls_yr = 0
        average_yr_price = 0
        row_number -= 1
