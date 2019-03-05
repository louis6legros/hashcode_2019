from input import *

def score_submission(input_file):

    photo_set = parse_input(input_file)

    with open('./data/output/submission_' + input_file + '.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    slides = lines[1::]
    score = 0
    for s1, s2 in zip(slides[:-1], slides[1::]):
        tags1 = []; tags2 = []
        for img in s1.split(' '):
            tags1 += photo_set.photos[int(img)].tags
        for img in s2.split(' '):
            tags2 += photo_set.photos[int(img)].tags

        tagsonly1 = len([t for t in tags1 if t not in tags2])
        tagsonly2 = len([t for t in tags2 if t not in tags1])

        common_tags = len(set([t for t in tags1 if t in tags2] + [t for t in tags2 if t in tags1]))

        score += min([common_tags, tagsonly1, tagsonly2])

    return score

def score_pictures(p1, p2):

    tags1 = p1.tags
    tags2 = p2.tags

    tagsonly1 = len([t for t in tags1 if t not in tags2])
    tagsonly2 = len([t for t in tags2 if t not in tags1])

    common_tags = len(set([t for t in tags1 if t in tags2] + [t for t in tags2 if t in tags1]))

    return min([tagsonly1, tagsonly2, common_tags])
