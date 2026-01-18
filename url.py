

url = input("enter link: ")

if "www." not in url:
    url = "https://www." + url

if "https://" not in url:
    url = "https://" + url

if ".com" not in url:
    url = url + ".com"

print(url)
