# This script creates a mip map from a given image
# minimal image width 1920px
#
# Usage:
# python3 mipMapGen.py <image path> <destination path (optional)>

from sys import argv
from PIL import Image
import re


ORIGINAL_IMAGE = argv[1]
DESTINATION_PATH = argv[2] if len(argv) >= 3 else "."


def get_image_name(image_path):
    image_name = image_path
    image_name = re.sub("[a-zA-Z:]*\\\\", "", image_name)
    image_name = re.sub("\.[A-z]*", "", image_name)
    return image_name


def createJSON(image_name, extension):
    json = "{\n\t\"bilder\": [\n"
    json+= "\t\t\"" + image_name + "_2xl." + extension + "\",\n"
    json += "\t\t\"" + image_name + "_xl." + extension + "\",\n"
    json += "\t\t\"" + image_name + "_lg." + extension + "\",\n"
    json += "\t\t\"" + image_name + "_md." + extension + "\",\n"
    json += "\t\t\"" + image_name + "_sm." + extension + "\",\n"
    json += "\t\t\"" + image_name + "_mobile." + extension + "\"\n"
    json += "\t]\n}"
    with open(image_name + ".json", "w") as file:
        file.write(json)
    return json


def create_mipmap(image_path, destination):
    image = Image.open(image_path)
    image.thumbnail((1920, 1920))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_2xl." + image.format.lower())
    image.thumbnail((1536, 1536))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_xl." + image.format.lower())
    image.thumbnail((1280, 1280))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_lg." + image.format.lower())
    image.thumbnail((1024, 1024))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_md." + image.format.lower())
    image.thumbnail((768, 768))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_sm." + image.format.lower())
    image.thumbnail((640, 640))
    image.save(destination + "/" + get_image_name(ORIGINAL_IMAGE) + "_mobile." + image.format.lower())


def main():
    create_mipmap(ORIGINAL_IMAGE, DESTINATION_PATH)
    print(createJSON(get_image_name(ORIGINAL_IMAGE), Image.open(ORIGINAL_IMAGE).format.lower()))


if __name__ == '__main__':
    main()
