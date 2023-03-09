######################################################
# Name: Hamza Fareed Ahmed Syed
# Project: <Image Manipulation Project using Python>
# Code URL: <https://replit.com/@HamzaFareed/ImageManipulation-PyhtonProject#main.py>

#Project Description:
# -- This project was made using Python to manipulate images instead of using Photoshop or any other editors.
# -- A collage that contains an original image and 8 modified versions of that image in a 3x3 grid.
# -- A collage that includes inverted, gray scaled, flipped, rotated, mirrored and cropped images.
# -- This project includes combination of blocks, conditional statements and loops.
######################################################

#Import
from PIL import Image

#Setting up the collage grid
grid = Image.new('RGB', (900, 900),
                 (255, 255, 255))  #set the collage bhg to plain white
grid.save("Collage_grid.jpg")

xg, yg = grid.size

#IMAGES OPENED
naruto = Image.open("Naruto.jpg")
g_scale = Image.open("Naruto.jpg")
rotate = Image.open("Naruto.jpg")
blue = Image.open("Naruto.jpg")
reflect = Image.open("Naruto.jpg")
naruto_h = Image.open("Naruto.jpg")
# red = Image.open("flipped_h.jpg")
img = Image.open("Naruto.jpg")
inverted = Image.open("Naruto.jpg")
red = Image.open("flipped_h.jpg")
w, h = naruto.size


#COPY IMAGE FUNCTION
def copy_image(img):
  copy = Image.new(img.mode, img.size)
  w, h = copy.size

  for x in range(w):
    for y in range(h):

      copy.putpixel((x, y), img.getpixel((x, y)))


copy_image(img)

# G R A Y S C A L E   F U N C T I O N


def grayscale():
  w, h = g_scale.size

  #print(g_scale.mode)

  for x in range(w):

    for y in range(h):

      r, g, b = g_scale.getpixel((x, y))

      avg = int((r + g + b) / 3)

      g_scale.putpixel((x, y), (avg, avg, avg))

  g_scale.save("gray.jpg")


grayscale()

#ROTATING IMAGE 90 DEGREE FUNCTION


def rotation():
  for x in range(w):
    for y in range(h):

      color = naruto.getpixel((x, y))
      target_x = (w - 1) - y
      target_y = x

      rotate.putpixel((target_x, target_y), color)
  rotate.save("rotate.jpg")


rotation()


# BLUE SHIFT FUNCTION
def blue_screen():
  #blue_2 = Image.new("RGB", blue.size, (0, 100, 0))

  w, h = blue.size
  #print(blue.size)
  for x in range(w):

    for y in range(h):

      if blue.mode == 'RGB':
        r, g, b = naruto.getpixel((x, y))
        r2 = 0
        g2 = 0
        b2 = 255 - b
        blue.putpixel((x, y), (r2, g2, b2))
      else:
        r, g, b, a = naruto.getpixel((x, y))
        if a != 0:
          ri = 0
          gi = 0
          bi = 200 - b
          blue.putpixel((x, y), (ri, gi, bi))
  blue.save("blue_naruto.jpg")


blue_screen()


#INVERT COLOR FUNCTION
def invert_colors():
  #inverted = Image.new(naruto.mode, naruto.size)
  w, h = inverted.size
  for x in range(int(w)):
    for y in range(int(h)):
      if inverted.mode == 'RGB':
        r, g, b = naruto.getpixel((x, y))
        r2 = 255 - r
        g2 = 255 - g
        b2 = 255 - b
        inverted.putpixel((x, y), (r2, g2, b2))
      else:
        r, g, b, a = inverted.getpixel((x, y))
        if a != 0:
          ri = 255 - r
          gi = 255 - g
          bi = 255 - b
          inverted.putpixel((x, y), (ri, gi, bi))
  inverted.save("invert_naruto.jpg")


invert_colors()


#CREATING MIRROR IMAGE OvER Y AXIS
def mirror_over_y():

  for x_reflect in range(w):
    for y_reflect in range(h):

      mirror_y = (h - 1) - y_reflect

      mr = reflect.getpixel((x_reflect, y_reflect))
      reflect.putpixel((x_reflect, mirror_y), mr)
      reflect.putpixel((x_reflect, mirror_y), mr)

  reflect.save("mirror_naruto.jpg")


mirror_over_y()

flipped_h = Image.new(naruto_h.mode, naruto_h.size, (255, 255, 0))


#function for horizontal flip
def flipped_horizontally():
  for x in range(int(w / 2)):
    for y in range(h):

      flip_x = (w - x) - 1

      flip = naruto_h.getpixel((flip_x, y))
      flipped_h.putpixel((flip_x, y), naruto_h.getpixel((x, y)))
      flipped_h.putpixel((x, y), flip)

  flipped_h.save("flipped_h.jpg")


flipped_horizontally()


#RED SCREEN + FLIPPED
def red_screen():
  # red = Image.open("flipped_h.jpg")
  # red = Image.new("RGB", red.size, (0, 0, 255))

  w, h = red.size

  #print(blue.mode)

  for x in range(w):

    for y in range(h):

      if red.mode == 'RGB':
        r, g, b = red.getpixel((x, y))
        r2 = 255 - r
        g2 = 0
        b2 = 0
        red.putpixel((x, y), (r2, g2, b2))
      else:
        r, g, b, a = red.getpixel((x, y))
        if a != 0:
          ri = 255 - r
          gi = 0
          bi = 0
          red.putpixel((x, y), (ri, gi, bi))
  red.save("red_naruto.jpg")


red_screen()

inverse_rotation = Image.new(naruto.mode, naruto.size, (0, 255, 0))


#function for rotating the image 180 degrees
def half_rotation():
  for y in range(int(h / 2)):
    for x in range(w):

      half_y = (h - 1) - y
      color = naruto.getpixel((x, y))
      rotation = naruto.getpixel((x, half_y))

      inverse_rotation.putpixel((x, half_y), color)
      inverse_rotation.putpixel((x, y), rotation)

  inverse_rotation.save("rotation_half.jpg")


half_rotation()


#function for pasting the images into the collage
def paste_image(source, destination, coordinates=(0, 0)):

  source_w, source_h = source.size
  dest_w, dest_h = destination.size
  x_coord, y_coord = coordinates

  for x in range(source_w):
    for y in range(source_h):

      px = source.getpixel((x, y))
      target_x = x + x_coord
      target_y = y + y_coord

      destination.putpixel((target_x, target_y), px)

  return destination


# collage = copy_image(grid)
# collage.save('collage.jpg')


#MAIN COLLAGE
def main():
  image_1 = paste_image(img, grid, (0, 0))

  image_2 = paste_image(g_scale, grid, (300, 0))

  image_3 = paste_image(inverted, grid, (600, 0))

  image_4 = paste_image(blue, grid, (0, 300))

  image_5 = paste_image(reflect, grid, (300, 300))

  image_6 = paste_image(red, grid, (600, 300))

  image_7 = paste_image(flipped_h, grid, (0, 600))

  image_8 = paste_image(rotate, grid, (300, 600))

  image_9 = paste_image(inverse_rotation, grid, (600, 600))

  #Evenly spaced it so it's easier to edit it
  image_9.save("collage.jpg")

  print("Name: Hamza Fareed Ahmed Syed")
  print("Image Manipulation Project using Python")


main()
