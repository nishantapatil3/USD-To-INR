from influxdb import InfluxDBClient

USER = 'root'
PASSWORD = 'root'
DBNAME = 'rates'
host = 'localhost'
port = 8086

client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
# client.drop_database(DBNAME)
client.create_database(DBNAME)
# client.switch_database(DBNAME)
# client.create_retention_policy('awesome_policy', '2d', 3, default=True)

tag_dic = {
            "host": "server01",
            "region": "us-west"
        }
field_dic = {
            "value": 0.64
        }

json_body = [
    {
        "measurement": "rate",
        "tags": tag_dic,
        "time": "2009-11-10T23:00:00Z",
        "fields": field_dic
    }
]

print client.write_points(json_body)
# flag2=flag2-1
# count=count+1
# print count
# tagdic.clear()				#clear dictionary
# fielddic.clear()

result = client.query('select * from rate;')
print("Result: {0}".format(result))

