import sys
from photo import *

def parse_orientation(o):
    if o == Orientation.HORIZONTAL.value:
        orientation = Orientation.HORIZONTAL
    elif o == Orientation.VERTICAL.value:
        orientation = Orientation.VERTICAL
    else:
        print('Wrong orientation value {}'.format(o))
        sys.exit()
    return orientation

def parse_input(data_set_name):
    fname = './data/input/'+data_set_name+'.txt'
    # read the file content as a list of strings
    # also strip out end-line characters '\n'
    with open(fname) as file:
        lines = [line.rstrip('\n') for line in file]
    num_photos = int(lines[0])
    photo_set = PhotoSet(num_photos)
    for i in range(1, len(lines)):
        photo_id = i-1
        items = lines[i].split()
        orientation = parse_orientation(items[0])
        num_tags = int(items[1])
        tags = [items[j] for j in range(2, 2+num_tags)]
        photo_set.add_photo(Photo(photo_id, orientation, num_tags, tags))
    return photo_set

def make_chunks(photo_set, nb_chunks=None):

    #  if no chunk size is specified, default is 1000
    if nb_chunks is None:
        print('toto')
        nb_chunks = len(photo_set.photos) // 1000

    # We have to make sure the number of vertical photos in each chunk is even
    chunks = []
    current_index = 0
    step = len(photo_set.photos) // nb_chunks
    for i in range(nb_chunks):
        tmp_photos = photo_set.photos[current_index:current_index+step]
        current_index += step
        nb_vertical_photos = len([photo for photo in tmp_photos if photo.orientation == Orientation.VERTICAL])
        while nb_vertical_photos % 2 != 0:
            tmp_photos.append(photo_set.photos[current_index])
            nb_vertical_photos = len([photo for photo in tmp_photos if photo.orientation == Orientation.VERTICAL])
            current_index += 1
        new_photo_set = PhotoSet(len(tmp_photos))
        for photo in tmp_photos:
            new_photo_set.add_photo(photo)
        chunks.append(new_photo_set)
    return chunks
