import requests
#J7d9EzrNnyxARzVOi+A5XQ==11fqoH84VGaJGJ3q
api_url = 'https://api.api-ninjas.com/v1/imagetotext'
image_file_descriptor = open('img-with-txt.png', 'rb',)
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files,headers={'X-Api-Key': 'J7d9EzrNnyxARzVOi+A5XQ==11fqoH84VGaJGJ3q'})
for i in r.json():
    print(i["text"],end=" ")
