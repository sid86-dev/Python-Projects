from requests import*
from urllib.request import urlopen

headers = {
  'Content-Type': 'application/json',
  'x-user-ip': '\'192.168.99.1\'',
  'x-api-key': '\'cRbHFJTlL6aSfZ0K2q7nj6MgV5Ih4hbA2fUG0ueO\''
}
request = Request('https://sandboxapi.coinswitch.co/v1/coins', headers=headers)

response_body = urlopen(request).read()
print(response_body)