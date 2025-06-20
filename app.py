#export INFLUXDB_TOKEN=hmS3nvbFXF_iGNJNysrRDXB8ITXUfrp_giVpwnFHPUfIY_9t1Uwh31sm6vnsVD9m1tnk6deQXIWbimjiKjSD2w==
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "myorg"
url = "127.0.0.1:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="mydata"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(10):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field2", value)
  )
  write_api.write(bucket=bucket, org="myorg", record=point)
  print(value)
  time.sleep(0.5) # separate points by 1 second
