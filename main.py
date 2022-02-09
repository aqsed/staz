import json
from datetime import datetime

f = open('data.json')

unique_users = set()
unique_orders = set()
requests_count_variant = {}
data = json.load(f)

for key, value in data.items():
    unique_users.add(key)

    for item_key, item_value in data[key].items():
        if item_key not in ('variant', 'similarInJsonList', 'NotEnoughSimilarsInStock'):
            if data[key]["variant"][0] == "similarInJsonList":
                if item_key not in requests_count_variant:
                    requests_count_variant[item_key] = 1
                else:
                    requests_count_variant[item_key] += 1

            unique_orders.add(item_key)

            # array to store time request values to determine median
            date_times = []

            old_date = ""
            count = 0
            sum = 0

            for i in range(len(item_value[0]) - 1, -1, -1):
                curr_date = datetime.fromisoformat(item_value[0][i][0])

                if old_date != "":
                    sum = (old_date.hour - curr_date.hour) * 3600 + (old_date.minute - curr_date.minute) * 60 + (old_date.second - curr_date.second)
                    date_times.append(sum)
                    count += 1

                old_date = curr_date

            if count != 0:
                print("AVG time for ", key, sum/count, "seconds")

            if len(date_times) > 0:
                print("median is:", date_times[int(len(date_times)/2)])

print("Number of unique users", len(unique_users))
print("Number of unique orders", len(unique_orders))
print("Number of request for orders:",requests_count_variant)