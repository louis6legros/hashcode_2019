from slide import *
from photo import *
from scoring import *

def create_dummy_slides(pset):
    """ Dummy slideshow where we first create Monoptychs with
    all horizontal photos and then Diptychs with all vertical
    photos in the same order as they appear in the input file
    """
    photos = pset.photos
    horizontals = [p for p in photos if p.orientation == Orientation.HORIZONTAL]
    verticals = [p for p in photos if p.orientation == Orientation.VERTICAL]
    slides = [Monoptych(p.id) for p in horizontals]
    diptychs = zip(*[iter(verticals)]*2)
    slides += [Diptych(d[0].id, d[1].id) for d in diptychs]
    return slides

def create_less_dummy_slides(pset, ):
    """ Starting with photo 0, we chose the photo than maximizes the score with
    photo 0 on the next slide, and so on...
    """

    photos = pset.photos
    if len(photos) == 0:
        return None

    scores = [[(p2.id, score_pictures(p1, p2)) for p2 in photos if p2 != p1] for p1 in photos]
    print('Pair scores successfully computed !')
    first = photos[0].id
    if photos[0].orientation == Orientation.HORIZONTAL:
        slides = [Monoptych(photos[0].id)]

        for line in scores:
            for score in line:
                if score[0] == first:
                    line.remove(score)
    else:
        # find another vertically oriented picture

        for line in scores:
            for score in line:
                if score[0] == first:
                    line.remove(score)
        for candidate in scores[0]:
            if photos[candidate[0]-first].orientation == Orientation.VERTICAL:
                slides = [Diptych(first, candidate[0])]
                break
        for line in scores:
            for s in line:
                if s[0] == candidate[0]:
                    line.remove(s)


    while len(scores[0]) > 1:
        # chose next picture
        current_slide = slides[-1]
        current_slide_id = int(current_slide.serialize().split(' ')[-1])
        next_slide = max(scores[current_slide_id-first], key=lambda x: x[1])
        if photos[next_slide[0]-first].orientation == Orientation.HORIZONTAL:
            slides.append(Monoptych(next_slide[0]))
            # remove next photo from potential candidates
            for line in scores:
                for score in line:
                    if score[0] == next_slide[0]:
                        line.remove(score)

        else:
            #  look for vertically oriented picture

            for line in scores:
                for score in line:
                    if score[0] == next_slide[0]:
                        line.remove(score)
            for candidate in scores[next_slide[0]-first]:
                if photos[candidate[0]-first].orientation == Orientation.VERTICAL:
                    slides.append(Diptych(next_slide[0], candidate[0]))
                    break
            for line in scores:
                for s in line:
                    if s[0] == candidate[0]:
                        line.remove(s)
    return slides
