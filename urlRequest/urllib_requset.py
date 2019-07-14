import urllib.request

response = urllib.request.urlopen("http://www.sicp.edu.cn")
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
print(response.getheader('Server'))