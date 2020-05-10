import json

f = open('logfile.txt', 'a')
log_data = {"productname": "example", "material": "example", "amount": 0.00}
json.dump(log_data, f)

#f.write('{}\n')
f.close()