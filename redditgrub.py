import urllib.request, json
import PIL
from PIL import Image
import os

print("getting meme...")

with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme") as url:
    data = json.loads(url.read().decode())
    print("meme aquired")
    urllib.request.urlretrieve(data["url"], "meme.jpg")
    
    print("resizing image...")
    img = Image.open("meme.jpg")
    img = img.resize((640, 480), PIL.Image.ANTIALIAS)
    img.save("meme_resized.jpg")
    
    print("moving to grub directory (/boot/grub/)...")
    os.system("sudo cp meme_resized.jpg /boot/grub/")
    
    print("updating grub...")
    os.system("sudo update-grub");