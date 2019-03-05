import sys
from enum import Enum

class Slide:

    def __init__(self, num_photos):
        pass

    def serialize(self):
        pass

class Monoptych(Slide):
    """ A slide with only one photo """
    def __init__(self, photo_1):
        self.photo_1 = photo_1

    def serialize(self):
        return str(self.photo_1)

class Diptych(Slide):
    """ A slide with two photos """
    def __init__(self, photo_1, photo_2):
        self.photo_1 = photo_1
        self.photo_2 = photo_2
    def serialize(self):
        return str(self.photo_1) + ' ' + str(self.photo_2)

class Submission:

    def __init__(self, data_set_name, slides):
        self.data_set_name = data_set_name
        self.slides  = slides
        self.num_slides = len(slides)

    def serialize(self):
        """ Convert Submission object to a list of strings """
        content = [str(self.num_slides)]
        for s in self.slides:
            content += [s.serialize()]
        return content

    def write_submission(self):
        filename = './data/output/submission_' + self.data_set_name + '.txt'
        with open(filename, 'w') as f:
            for item in self.serialize():
                f.write("%s\n" % item)
        print('Successfully wrote submission file {}'.format(filename))
