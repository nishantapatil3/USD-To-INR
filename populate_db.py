import datetime
# from fixerio import Fixerio
from influxdb import InfluxDBClient
from get_exchange_info import *
import sched, time

s = sched.scheduler(time.time, time.sleep)

USER = 'root'
PASSWORD = 'root'
DBNAME = 'rates'
host = '127.0.0.1'
port = 8086

client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
# client.drop_database(DBNAME)
# client.create_database(DBNAME)
# client.switch_database(DBNAME)
# client.create_retention_policy('one month', '30d', 3, default=True)

num_days = 1000

"""
def get_usd_inr_history(day):
    rates = Fixerio(base='USD', symbols=['USD', 'INR'])
    return rates.historical_rates(day)


def populate_db_history():
    rate_dict = {}
    base = datetime.date.today()
    dates = [base - datetime.timedelta(days=x) for x in range(0, num_days)]

    for day in dates:
        rate_dict = get_usd_inr_history(day)
        print rate_dict

        json_body = [
            {
                "measurement": "rate",
                "tags": {"Currency": "INR"},
                "time": rate_dict["date"] + "T00:00:00Z",
                "fields": rate_dict["rates"]
            }
        ]
        print client.write_points(json_body)
"""

def populate_db_current(sc):
    rate_dict = {}
    date_time = datetime.datetime.today()

    current_rate = get_google_exchange()
    
    json_body = [
            {
                "measurement": "rate",
                "tags": {"Currency": "INR"},
                "time": date_time,
                "fields": {"INR": current_rate}
            }
        ]

    print client.write_points(json_body)
    s.enter(300, 1, populate_db_current, (sc,))

def main():
    #populate_db_current()
    s.enter(1, 1, populate_db_current, (s,))
    s.run()


if __name__ == '__main__':
    main()
