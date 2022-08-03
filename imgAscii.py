from PIL import Image
import numpy as np


# Change these for small changes
character_compensator = (2.2,1)
resolution_multiplier = 0.5

# First step is to make the image into Luminance mode by applying .convert("L")
# Then we can cycle though the pixels, assigning a different ASCII char depening on 
# what value the Luminance is (0,255).

# characters = [[" ", 0], [".", 8], [":", 16], ["^", 20], ["~", 25], ["!", 30], ["7", 37], ["?", 44], ["J", 50], ["Y", 55], ["5", 60], ["P", 68], ["G", 75], ["B", 80], ["&", 86], ["#", 90], ["@", 100]]

# def to_percent(num, total):
#     return (num/100)*total


def pixel_iter(image):
    piX,piY = image.size
    result = ""

    for y in range(piY):
        for x in range(piX):
            lumin = image.getpixel((x,y))
            if lumin == 0: result += " "
            elif lumin <= 16: result += "."
            elif lumin <= 32: result += ":"
            elif lumin <= 48: result += "^"
            elif lumin <= 64: result += "~"
            elif lumin <= 80: result += "!"
            elif lumin <= 96: result += "7"
            elif lumin <= 112: result += "?"
            elif lumin <= 128: result += "J"
            elif lumin <= 144: result += "Y"
            elif lumin <= 160: result += "5"
            elif lumin <= 176: result += "P"
            elif lumin <= 192: result += "G"
            elif lumin <= 208: result += "B"
            elif lumin <= 224: result += "#"
            elif lumin <= 240: result += "&"
            else: result += "@"
            # for i in range(len(characters)):
            #     if lumin >= to_percent(characters[i][1], 255): 
            #         result += characters[i][0]
            #         break
        
        result += "\n"
    return result

def ratio_resize(image, char_compensator = (1.9,1), max_size=(104,55)):
    width,height = image.size
    ratio = min(max_size[0]/width, max_size[1]/height)
    new_width, new_height = (width*ratio*char_compensator[0]*resolution_multiplier, height*ratio*char_compensator[1]*resolution_multiplier)
    image = image.resize((int(new_width),int(new_height)), Image.Resampling.LANCZOS)
    return image

def color_transparency(image):
    ctX,ctY = image.size
    try:
        image = image.convert("RGBA")
        for x in range(ctX):
            for y in range(ctY):
                if image.getpixel((x,y)) == (0,0,0,0):
                    image.putpixel((x,y), (255,255,255,255))
        return image
    except Exception as e:
        print("Could not convert into rgba, continuing with black transparancy")
        return image

def find_transparency(image):
    if image.info.get("transparency", None) is not None:
        return True
    if image.mode == "P":
        transparent = image.info.get("transparency", -1)
        for _, index in image.getcolors():
            if index == transparent:
                return True
    elif image.mode == "RGBA":
        extrema = image.getextrema()
        if extrema[3][0] < 255:
            return True

    return False

image_path = input("Drag and drop the image or white the image path\n")

def main():
    try:
        image = Image.open(image_path.replace(" ", ""))
        #find and color transparency
        if find_transparency(image):
            transparent_white = True if "y" == input("Do you want to make the transparent background white? (y/n)\n") else False
            image = color_transparency(image) if transparent_white else image
        
        image = image.convert("L")
        image = ratio_resize(image, character_compensator)
        image = pixel_iter(image)
        print(image)
        print()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()