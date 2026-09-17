import sys
try:
    from PIL import Image
    
    img = Image.open('images/logo.png').convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # If pixel is white or very close to white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    
    # Get the bounding box of the non-transparent alpha channel
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save('images/logo_clean.png', "PNG")
    print("Logo processed successfully!")
    
except ImportError:
    print("Pillow is not installed. Please install it.")
