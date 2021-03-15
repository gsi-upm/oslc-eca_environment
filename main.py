import json

with open('./services.json') as f:
    services = json.load(f)

print(services)