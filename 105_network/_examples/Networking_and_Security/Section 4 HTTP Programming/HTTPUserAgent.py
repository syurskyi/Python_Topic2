import httplib

h = "www.infiniteskills.com"

req = httplib.HTTP(h)
req.putrequest("GET", "/")
req.putheader("Host", h)
req.putheader("User-Agent", "Garbage browser: 5.6")
req.putheader("My-Header", "My value")
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response: ", statusMsg)

