# /usr/bin/env python3

"""

Introduction:
This is a module containing a function "classify". It is a tool for the back-end program to classify trash by using the
Keras Sequential MODEL.

"""

__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"

from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
from imutils import paths
import numpy as np
from typing import NewType
from Error import InvalidInputError, InvalidImageError

# Load MODEL
MODEL = load_model("./MODEL.h5")

Path = NewType('path', str)


def classify(path: Path) -> str:
    """
    This is a function using the trained Keras Sequential MODEL to classify the input image.
    :param path: the path of image which is need to be classify
    :return prediction: the result of classification

    Doctest:
    >>> path = Path('test.jpg')
    >>> classify(path)
    Organic
    >>> classify(1)
    Traceback (most recent call last):
        ...
    exception.InvalidInputError
    >>> path1 = Path('None')
    >>> classify(path1)
    Traceback (most recent call last):
        ...
    exception.InvalidImageError
    """
    try:
        path += ''
        image = load_img(path, target_size=(64, 64))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        result = MODEL.predict(image)
        if result[0][0] == 1:
            result = 'Recyclable'
        else:
            result = 'Organic'
        return result
    except TypeError:
        raise InvalidInputError from None
    except FileNotFoundError:
        raise InvalidImageError from None


if __name__ == '__main__':
    test_path = "./DATASET/TEST"
    image_paths = sorted(list(paths.list_images(test_path)))
    for each in image_paths:
        print(classify(each))
