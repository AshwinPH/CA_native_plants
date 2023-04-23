import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import io
import re

# Define the URL of the webpage
url = "https://example.com"

# Send an HTTP request to the webpage and get the HTML content
#response = requests.get(url)
#html_content = response.content

# Parse the HTML content using Beautiful Soup

with open('Line-Drawings.html', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <img> tags in the HTML content
a_tags = soup.find_all('a')

print(f'Found html tags: {len(a_tags)}')
counter = 0
img_urls = []
labels = []
for link in a_tags:
    #print(link.get('href'))
    img_url = link.get('href')
    #label = link.get_text()
    label = re.sub(r"[^a-zA-Z0-9'\-\s_]", '', link.contents[-1])
    print(link.contents)
    img_urls.append(img_url)
    labels.append(label)

    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    img.save('images/' + labels[counter] + '.jpg')
    counter += 1

print(f'Extracted image links: {len(img_urls)}')

# images = []
# counter = 0
# for url in img_urls:
#     response = requests.get(url)
#     img = Image.open(io.BytesIO(response.content))
#     img.thumbnail((1000,1000))
#     images.append(img)
#     print(f'image opened: {counter}')
#     counter += 1

# print(f'Extracted image data: {len(images)}')

# # Calculate the width and height of the collage based on the number of images
# width = sum(img.width for img in images)
# height = max(img.height for img in images)
# print(f'Calculated collage dims: {width}, {height}')
# # # Create a new blank image for the collage
# unlabeled_collage = Image.new('RGB', (width, height), (255, 255, 255))
# print('Made blank image')
# # Paste each image into the collage
# counter = 0
# x_offset = 0
# for img in images:
#     unlabeled_collage.paste(img, (x_offset, 0))
#     print(f'Collaged {labels[counter]}')
#     #collage.text((x_offset,height-20), labels[counter], fill=(0,0,0))
#     x_offset += img.width
#     counter += 1


# # Save the collage as a file
# unlabeled_collage.save('unlabeled_collage.jpg')
# Image.MAX_IMAGE_PIXELS = None
# collage = Image.open('unlabeled_collage.jpg')
# canvas = ImageDraw.Draw(collage)

# fontSize = 30
# myFont = ImageFont.truetype('arial.ttf', fontSize)
# counter = 0
# x_offset = 0
# for img in images:
#     print(f'Labeled {labels[counter]}')
#     canvas.text((x_offset+20, height-(fontSize+20)), labels[counter], font = myFont, fill=(0,0,0))
#     x_offset += img.width
#     counter += 1
    
# collage.show()
# collage.save('collage.jpg')




