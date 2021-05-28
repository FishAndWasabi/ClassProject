# /usr/bin/env python3

"""

Introduction:
This is the Exception classes which is used in the Trash classification project.

"""

__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"


class InvalidInputError(TypeError):
    pass


class InvalidImageError(FileNotFoundError):
    pass


class CameraError(Exception):
    pass