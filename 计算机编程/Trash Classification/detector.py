# /usr/bin/env python3

"""

This is a module which implements the set and test of cameras installed on mechanisms.

"""

__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"

import cv2
import datetime
import time
import os
from Error import InvalidInputError,CameraError

MINSIZE = 1000


class Camera(cv2.VideoCapture):
    """
    This class is built for cameras which collects images for garbage put in defined surveillance areas.
    """

    def __init__(self, path=None):
        """
       Initialising the camera
       :param path: the directory of the camera which is used to store images taken by this camera
       """

        self.frame_id = 0
        if not path:
            super().__init__(0)
        else:
            try:
                path += ''
                super().__init__(path)
            except TypeError:
                raise InvalidInputError from None

    def test(self, times=40):
        """
        Testing whether the camera works normally, being able to monitor and take images.
        :param times: the times of testing
        """
        try:
            times += 0
            for i in range(times):
                ret = self.read()[0]
                if not ret:
                    raise CameraError from None
            return True
        except TypeError:
            raise InvalidInputError from None

    def detect(self, path):
        """
        Capture images when garbage appears in the defined surveillance area by detecting the frames which are obviously differs from previous ones.
        Then add timestamps for images and store images in the directory of the camera.
        :param path: the directory of the camera which is used to store images taken by this camera
        """
        first_frame = None
        total = 2000
        count = 2000
        # loop over the frames of the video
        while True:
            (grabbed, frame) = self.read()
            flag = False
            if not grabbed:
                time.sleep(10)
                continue
            frame_name = str(self.frame_id) + datetime.datetime.now().strftime(
                "%A_%d_%B_%Y_%I_%M_%S%p")
            # convert it to grayscale, and blur it
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            # update firstFrame for every while
            if count % total == 0:
                first_frame = gray
                count = (count + 1) % total
                continue
            else:
                count = (count + 1) % total
            # compute the absolute difference between the current frame and first frame
            frameDelta = cv2.absdiff(first_frame, gray)
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
            # dilate the threshold image, then find contours on it
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in cnts:
                # if the contour is too small, ignore it
                if cv2.contourArea(cnt) >= MINSIZE:
                    (x, y, w, h) = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    flag = True
                    # add the timestamp on the frame
                    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                                (10, frame.shape[0] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            if flag:
                cv2.imwrite(os.path.join(path, frame_name) + '.jpg', frame)
                self.frame_id += 1
                # Wait for next piece of garbage
                time.sleep(10)
            # if the 'q' key is pressed, stop the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

    def stop(self):
        """
        Defining the operation of shutting down the camera.
        Cleanup the camera and close any open windows.
        """
        self.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    path = 'tmp'
    c1 = Camera()
    c1.test()
    c1.detect(path)
    c1.stop()
