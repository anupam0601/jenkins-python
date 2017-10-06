prom_alerts = {
    "status": "success",
    "data": [
        {
            "labels": {
                "alertname": "HighCpu",
                "instance": "192.168.56.102:9100",
                "severity": "warning"
            },
            "annotations": {
                "description": "CPU usage high",
                "summary": "CPU usage high"
            },
            "startsAt": "2017-08-02T03:33:52.804Z",
            "endsAt": "2017-08-02T03:43:22.808615086Z",
            "generatorURL": "http://auto1234:9090/graph?g0.expr=100+%2A+%281+-+avg%28irate%28node_cpu%7Binstance%3D%22192.168.56.102%3A9100%22%2Cjob%3D%22node%22%2Cmode%3D%22idle%22%7D%5B5m%5D%29%29+BY+%28instance%29%29+%3E+0\u0026g0.tab=0",
            "status": {
                "state": "active",
                "silencedBy": [

                ],
                "inhibitedBy":[

                ]
            },
            "receivers":[
                "team-X-mails"
            ]
        },
        {
            "labels": {
                "alertname": "InstanceDown",
                "instance": "192.168.56.102:9100",
                "severity": "warning"
            },
            "annotations": {
                "description": "CPU usage high",
                "summary": "CPU usage high"
            },
            "startsAt": "2017-08-02T03:24:53.973Z",
            "endsAt": "2017-08-02T03:43:22.809437751Z",
            "generatorURL": "http://auto1234:9090/graph?g0.expr=100+%2A+%281+-+avg%28irate%28node_cpu%7Binstance%3D%22192.168.56.102%3A9100%22%2Cjob%3D%22node%22%2Cmode%3D%22idle%22%7D%5B5m%5D%29%29+BY+%28instance%29%29+%3E+0\u0026g0.tab=0",
            "status": {
                "state": "active",
                "silencedBy": [

                ],
                "inhibitedBy":[

                ]
            },
            "receivers":[
                "team-X-mails"
            ]
        }
    ]
}

# print prom_alerts["data"]


alerts_metadata = {}

"""
Form a dict with unique keys and values:
alerts_metadata[alert["labels"]["alertname"]]
- key for dict alerts_metadata = {}
"""

for alert in prom_alerts["data"]:
    alerts_metadata[alert["labels"]["alertname"]] = {"instance_name": alert[
        "labels"]["instance"], "alert_status": alert["status"]["state"]}

print alerts_metadata

count = 0
for alert, status in alerts_metadata.iteritems():
	if status['alert_status'] == 'active':
		print status
		count = count + 1
print count