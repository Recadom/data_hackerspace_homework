#Martynas Juskelis

import json
import numpy
import csv


def histogram_times(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    f.close()

    hist = [0] * 24
    times = [row[1] for row in airplane_data[1:] if row[1] != '']

    for t in times:
        hour = t.split(':')[0]
        if hour.isdigit() and int(hour) < len(hist):
            hist[int(hour)] = hist[int(hour)] + 1

    return hist


def weigh_pokemons(filename, weight):
    with open(filename) as f:
        data = json.load(f)
    f.close()
    ans = []

    for pokemon in data['pokemon']:
        if float(pokemon['weight'].split(' ')[0]) == weight:
            ans.append(pokemon['name'])

    return ans


def single_type_candy_count(filename):
    #open file
    with open(filename) as f:
        data = json.load(f)
    f.close()
    #initialize total
    total = 0

    #count total
    for pokemon in data["pokemon"]:
        if len(pokemon["type"]) == 1 and "candy_count" in pokemon:
            total += pokemon["candy_count"]
    return total


def reflections_and_projections(points):
    newPoints = []

    for point in points:
        #Flip/reflecy over y=1
        newPoint = [point[0], 2 - point[1]]

        #Rotate π/2 radians (90 degrees)
        rotateAng = numpy.pi / 2

        #Set Up Array
        newPoint = [newPoint[0] * numpy.cos(rotateAng) - newPoint[1] * numpy.sin(rotateAng), newPoint[0] * numpy.sin(rotateAng) + newPoint[1] * numpy.cos(rotateAng)]

        # Project to y = 3x
        lineProjScalar = 3
        scaleFactor = 1 / (lineProjScalar ** 2 + 1)

        newPoint = [round(scaleFactor * (newPoint[0] + newPoint[1] * lineProjScalar), 2), round(scaleFactor * (newPoint[0] * lineProjScalar + newPoint[1] * (lineProjScalar ** 2)), 2)
        ]

        newPoints.append(newPoint)

    return numpy.array(newPoints)


def normalize(image):
    return (255 / (image.max() - image.min())) * (image - image.min())


def sigmoid_normalize(image, a):
    mult = ((numpy.e ** (-1 * (a ** -1) * (image - 128)) + 1) ** -1)
    return 255 * mult
