# /usr/bin/env python3

"""

This is a module for the backend of trash classification.
There is a class "Classifier" which inherits Thread class
and a function "backend_process" which is a concurrency and circulate process.

"""

__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"

from classify import classify,Path
import time
import os
from threading import Thread, Lock
import datetime
from shutil import copy

# The path of photos(from each camera)' storage location: \tmp\cameraId\imgs
PATH = 'tmp\\'


class Classifier(Thread):
    """
    This is class inherit threading.Thread class which is used to classify image.
    """
    count = 0
    lock = Lock()

    def __init__(self, cameraId: str, imagesName: list):
        """
        Initialising the thread
        :param cameraId: cameraId is the unique identity of each camera. The cameraId is the name of the camera's dir.
        :param imagesName: The list of the images name.
        """
        Thread.__init__(self)
        self.cameraId = cameraId
        self.cameraPath = os.path.join('result', self.cameraId)
        os.mkdir(self.cameraPath)
        self.imagesName = imagesName

    def run(self):
        """
        Run the thread
        This is the execution of the thread.Each thread classifies images of one camera directory.
        """
        for imageName in self.imagesName:
            imagePath = os.path.join(PATH, self.cameraId, imageName)
            # Initialising the thread's lock
            Classifier.lock.acquire(timeout=30)
            if Classifier.lock.locked():
                # Start
                stime = datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%S%p")
                # Classify
                imagePath = Path(imagePath)
                result = classify(imagePath)
                # Store in different dirs (cameraId\result\img)
                new_imageName = str(Classifier.count) + '_' + stime + '.jpg'
                new_imagePath = self.cameraPath + '\\' + result
                if not os.path.exists(new_imagePath):
                    os.mkdir(new_imagePath)
                copy(imagePath, os.path.join(new_imagePath, new_imageName))
                # Send flag to the actuators
                send(result)
                # Delete the image which is processed
                os.remove(imagePath)
                # End time
                etime = datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%S%p")
                # Write log
                with open('log.txt', 'a+') as fw:
                    fw.write("Start:%s" % stime + ' ' + self.cameraId + '\n')
                    fw.write("Image: " + imageName + '\n')
                    fw.write("Result: " + result + '\n')
                    fw.write("End:%s" % etime + ' ' + self.cameraId + '\n')
                    fw.write('-----------------------' + '\n')
                Classifier.count += 1
                Classifier.lock.release()



def send(result):
    """
    Imitate transfer information between the back-end and the actuators
    The actuators are mechanisms that receive the returned signal and send the garbage to different bins.
    :param result: The catagory which is the classify result of the image.
    """
    if result == 'Recyclable':
        return True
    else:
        return False


def backend_process():
    """
    This is the main process of the back-end.
    It circularly detects the camera's dirs and start the "Classifier" threads.
    In this way, it is able to classify all the images from various cameras.
    """
    os.mkdir('result')
    threads = []
    act_threads = []
    while True:
        dirs = os.listdir(PATH)
        if not dirs:
            print('No camera is running')
            time.sleep(10)
            continue
        # Remove the stop cameras
        for t in threads:
            if t.cameraId not in dirs:
                threads.remove(t)
                act_threads.remove(t)
                del t
        # Travel each camera
        for dir in dirs:
            cameraID = dir
            cameraPath = os.path.join(PATH, dir)
            imgs = os.listdir(cameraPath)
            # Check camera folder for pictures
            if imgs:
                # Check whether the camera has joined the process, if not, join
                if cameraID not in [t.cameraId for t in threads]:
                    exec('%s = classifier("%s",%s)' % (cameraID, cameraID, imgs))
                    exec('''threads.append(%s)''' % (cameraID))
        for t in threads:
            if not t in act_threads:
                act_threads.append(t)
                t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    backend_process()