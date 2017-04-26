import sys
import os
import io
import requests
from PIL import Image as PILImage
import tempfile

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

import requests

def diagonal(image):
    w,h = image.width, image.height
    ratio = max(w,h)/min(w,h)
    
    return (image.width**2 + image.height**2)/ratio

def resolve_url(page,src):
    srcbits = urlparse(src)
    if not srcbits.scheme:
        bits = urlparse(page)
        root = '/'.join(bits.path.split('/')[:-1])+'/'
        return urlunparse((bits.scheme,bits.netloc,root+src,'','',''))
    else:
        return src

def get_image(img_url):
    buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
    r = requests.get(img_url, stream=True,headers=headers)
    if r.status_code == 200:
        downloaded = 0
        filesize = int(r.headers['content-length'])
        for chunk in r.iter_content():
            downloaded += len(chunk)
            buffer.write(chunk)
        buffer.seek(0)
        image = PILImage.open(io.BytesIO(buffer.read()))
        #i.save(os.path.join(out_dir, 'image.jpg'), quality=85)
    else:
        return
    buffer.close()
    return image

def get_featured_image(page_url):
    r  = requests.get(page_url,headers=headers)
    data = r.text
    soup = BeautifulSoup(data,'lxml')

    image_urls = [resolve_url(page_url,image.get('src')) for image in soup.find_all('img')]
    images = [(url,get_image(url)) for url in image_urls]
    images = [(u,i) for u,i in images if i is not None]

    images.sort(key=lambda x: diagonal(x[1]),reverse=True)
    if len(images):
        return images[0]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == '__main__':
    page_url = sys.argv[1]
    url, image = get_featured_image(page_url)
    print(url)