import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

# Define the URL of the webpage
url = "https://example.com"

# Send an HTTP request to the webpage and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <img> tags in the HTML content
img_tags = soup.find_all('img')

# Create a list to store the image URLs
img_urls = []

# Extract the URL of each image and add it to the list
for img in img_tags:
    img_url = img['src']
    if img_url.startswith('http'):
        img_urls.append(img_url)

# Create a list to store the downloaded images
images = []

# Download each image and add it to the list
for url in img_urls:
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    images.append(img)

# Calculate the width and height of the collage based on the number of images
width = sum(img.width for img in images)
height = max(img.height for img in images)

# Create a new blank image for the collage
collage = Image.new('RGB', (width, height), (255, 255, 255))

# Paste each image into the collage
x_offset = 0
for img in images:
    collage.paste(img, (x_offset, 0))
    x_offset += img.width

# Save the collage as a file
collage.save('collage.jpg')
