import pyshorteners

s = pyshorteners.Shortener()
url = 'https://demos.creative-tim.com/material-dashboard-pro-react/?_ga=2.134180812.312426588.1627822858-69904067.1627585768#/admin/dashboard'
print(s.tinyurl.short(url))