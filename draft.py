import jellyfish
import numpy as np

# Example list of strings
strings = [
    "OPENING DATE       : 14/11/2011 ddqq",
    "OPENING DATE       : 05/01/2006",
    "OPENING DATE       : 19/10/2006 pdcw"
    "OPENING DATE       : 19/12/2009 lmpo"
    "OPENING DATA       : 19/12/2009"
]

import numpy as np


def centroid_string(strings, similarity_measure=jellyfish.jaro_distance):
    # Compute Jaro distance matrix
    jaro_distances = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(len(strings)):
            jaro_distances[i, j] = similarity_measure(strings[i], strings[j])

    # Compute mean Jaro distance for each string
    mean_jaro_distances = np.mean(jaro_distances, axis=1)
    # Choose string with highest mean Jaro distance as centroid
    centroid_index = np.argmax(mean_jaro_distances)
    return strings[centroid_index]


print(centroid_string(strings))
