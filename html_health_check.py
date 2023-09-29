from collections import defaultdict
import datetime
import requests
import sys
import time
import yaml

# raises an AssertionError if there is not exactly one input argument
assert len(sys.argv) == 2, 'Must pass a YAML file as an argument'

with open(sys.argv[1], 'r') as f:
    yaml_file = yaml.safe_load(f)

while True:
    t0 = time.time()
    total_requests = defaultdict(int)
    up_requests = defaultdict(int)

    for r in yaml_file:
        # get elements of request
        name = r['name'].split(' ')[0]
        if 'method' not in r:
            r['method'] = 'GET'
        additional_ele = {}
        if 'headers' in r:
            additional_ele['headers'] = r['headers']
        if 'body' in r:
            additional_ele['json'] = r['body']

        # send request
        response = requests.request(r['method'], r['url'], timeout=0.1, **additional_ele)

        # determine if UP or DOWN
        if (200 <= response.status_code <= 299 and 
                response.elapsed < datetime.timedelta(milliseconds=500)):
            up_requests[name] += 1
        total_requests[name] += 1

    # calculate and print availability
    for name in total_requests:
        availability = int(round(up_requests[name] / total_requests[name] * 100, 0))
        print(f'{name} has {availability}% availability percentage')
        
    time.sleep(15-max(0, time.time() - t0)) # calculate remaining time to sleep