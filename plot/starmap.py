'''
This is a series of functions to 
(a) parse some basic starmap data
(b) plot starmap data
'''
import csv
import Image
import picture

'''
@Read a file
@Return three dicts
'''
def read_coords(file):
    starfile = open(file, 'rb')
    starstuff = csv.reader(starfile, delimiter=' ')
    # x, y, z coords, henry draper number, magnitude, harvard revised number, list of names for a star
    starcoords = {}
    starlight = {}
    starnames = {}
    for row in starstuff:
        # only 0 - 5 options
        x = row[0]
        y = row[1]
        z = row[2]
        henrydraper = row[3]
        magnitude = row[4]
        harvard = row[5]
        try:
            names = row[6]
            names = names.split("; ")
	except:
            names = ()
        # 1st dictionary
        starcoords[henrydraper] = (x, y)
        # 2nd dictionary
        starlight[henrydraper] = magnitude
        # 3rd dictionary
        for name in names:
            starnames[name] = henrydraper
    starfile.close()
    return (starcoords, starlight, starnames)

# Debug
# print read_coords('stars.txt')

'''
Take a square picture object, size of picture in pixels, and dictionary of star values
Return a plot of the stars using the picture module
** use add_rect_filled
'''

def coords_to_pixel(orig_x, orig_y, size):
    
    return (x, y)

def plot_plain_stars(pic, width, starcoords):
    for henrydraper, coordinates in starcoords:
        x = coordinates[0]
        y = coordinates[1]
        add_rect_filled('#ffffff', x, y)
    return pic


