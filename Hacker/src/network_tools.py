'''
    Geolocalização do IP
    https://dev.maxmind.com/geoip/geolite2-free-geolocation-data
    https://www.automox.com/blog/visualizing-network-data-in-real-time-with-python
    https://python.plainenglish.io/network-traffic-analysis-with-python-f95ed4e76c28
'''

import geoip2.database

reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
response = reader.country('128.101.101.101')
print(response)