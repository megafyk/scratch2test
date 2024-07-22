import csv

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,vi;q=0.8,ja;q=0.7,ko;q=0.6,zh;q=0.5",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZXJJZCI6NjQsInJvbGVJZCI6MTAsInByb3ZpZGVySWQiOjAsInBhcnRuZXJJZHMiOltdLCJzY29wZSI6InVzZXIiLCJleHBpcmVBY2Nlc3NUb2tlbiI6MjE2MDAwLCJleHBpcmVSZWZyZXNoVG9rZW4iOjg2NDAwMDB9LCJpYXQiOjE3MjE2MTAzMDAsImV4cCI6MTcyMTgyNjMwMH0.TRK1fZCOllQXpCjkHuDxtIg1qCj9sD5rJFQ13QDADwg",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://vds-cms.mpoint.vn",
    "priority": "u=1, i",
    "referer": "https://vds-cms.mpoint.vn/",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

with open("data.csv", "r", newline="") as r_file:
    reader = csv.reader(r_file)

    with open("data_out.csv", "w", newline="") as w_file:
        writer = csv.writer(w_file)

        header = next(reader)

        header.append("status")
        header.append("data")
        writer.writerow(header)
        cnt = 0
        for row in reader:

            try:
                url = f"https://vds-backend-cms.mpoint.vn/api/paymentTransaction?page=282&api=find&queryInput=%7B%22transactionId%22%3A%7B%22contains%22%3A%22{row[9]}%22%7D%7D&limit=10&skip=0&sort=%5B%7B%22id%22%3A%22desc%22%7D%5D"
                response = requests.get(url=url, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    row.append(data["data"][0]["status"])
                    row.append(data)
                    writer.writerow(row)
                    print(f"done process {row[9]}")
            except Exception as e:
                print(cnt, e)
            cnt += 1
            if cnt % 10 == 0:
                print(f"finished {cnt} rows")
