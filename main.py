from input import *
from slide import *
from slideshow import *
from scoring import *


a = 'a_example'
b = 'b_lovely_landscapes'
c = 'c_memorable_moments'
d = 'd_pet_pictures'
e = 'e_shiny_selfies'

data_sets = [a, b, c, d, e]


for data_set in data_sets:
    photo_set = parse_input(data_set)
    chunks = make_chunks(photo_set, nb_chunks=1000)
    slides = []
    for chunk in chunks:
        slides += create_less_dummy_slides(chunk)
    submission = Submission(data_set, slides)
    submission.write_submission()

for data_set in data_sets:
    print(score_submission(data_set))

# # Test random arrangement of pictures...
# from random import shuffle
# shuffle(slides)
# new_submission = Submission(b, slides)
# new_submission.write_submission()
# score_submission(b)

def sanity_check(input_file):
    with open('./data/output/submission_' + input_file + '.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    lines = lines[1::]
    numbers = []
    for line in lines:
        numbers += line.split(' ')

    if len(set(numbers)) == len(numbers):
        return True
    else:
        return False
