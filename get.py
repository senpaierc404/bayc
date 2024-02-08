import requests

for i in range(100):
    image_url = 'https://boredapeyachtclub.com/_next/image?url=https%3A%2F%2Fassets.boredapeyachtclub.com%2Fbayc%2F' + str(i) + '.png&w=640&q=75'
    img_data = requests.get(image_url).content
    with open('bayc' +  str(i) + '.png', 'wb') as handler:
        handler.write(img_data)
