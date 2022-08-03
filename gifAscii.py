from PIL import Image, ImageOps
import math

# Change these for result changes
character_compensator = (2.7,1)
resolution_multiplier = 1
characters = [
             "@", "#", "&", "B", "0", "G", "5", "Y", "J", "?", "7", "*", "!", "~", "^", ":", ",", ".", " "
             ]
# characters = [" ", ".", ":", "^", "~", "!", "7", "?", "J", "Y", "5", "G", "B", "#", "&", "@"]

seq = []

def pixel_iter(image):
    piX,piY = image.size
    result = ""

    for y in range(piY):
        for x in range(piX):
            luminosity = image.getpixel((x,y))
            idx = int((luminosity / 255) * (len(characters)-1))
            result += characters[idx]
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


def main():
    try:
        # Inputs from user
        image_path = input("Drag and drop the image or white the image path\n")
        # invert = False
        image = Image.open(image_path.replace(" ", ""))
        # Find and color transparency
        if find_transparency(image):
            transparent_white = True if "y" == input("Do you want to make the transparent background white? (y/n)\n") else False
            image = color_transparency(image) if transparent_white else image
        
        image = image.convert("L")
        image = ratio_resize(image, character_compensator)
        image = pixel_iter(image)
        print(image)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()