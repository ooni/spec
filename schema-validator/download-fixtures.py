import requests
import random
import json

test_names = [
    "meek_fronted_requests_test",
    "web_connectivity",
    "dns_consistency",
    "http_requests",
    "http_host",
    "http_header_field_manipulation",
    "http_invalid_request_line",
    "tcp_connect",
    "multi_protocol_traceroute",
    "bridge_reachability",
    "vanilla_tor",
    "web_connectivity",
    "whatsapp",
    "facebook_messenger",
    "telegram",
    "dash"
]

def get_random_url(test_name):
    j = requests.get("https://api.ooni.io/api/v1/measurements?test_name={}".format(test_name)).json()
    return random.choice(j["results"])["measurement_url"]

for tn in test_names:
    url = get_random_url(tn)
    r = requests.get(url)
    j = r.json()
    with open('test-specs/{}.json'.format(tn), 'w') as out_file:
        json.dump(j, out_file, indent=2)
