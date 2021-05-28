# /usr/bin/env python3

"""

Introduction:
This module builds and trans the machine learning model for classification. The model is the keras Sequential model
which is good to the image classification.

"""

__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# The parameter of the model
TRAIN_PATH = os.path.join('DATASET', 'TRAIN')
TEST_PATH = os.path.join('DATASET', 'TEST')
BATCH_SIZE = 32
EPOCHS = 4
IMG_SIZE = 64


class Model(Sequential):
    """
    This class inherits the Keras Sequential model of the tensorflow and has three basic function: prepare_data, set and
    tran.
    The class does not have the certain output, therefore it does not have doctest.
    """
    # Prepare the dataset for training and testing.
    def prepare_data(self):
        # Dataset for training
        train_data = ImageDataGenerator(rescale=1. / 255)
        self.training_set = train_data.flow_from_directory(TRAIN_PATH,
                                                              target_size=(IMG_SIZE, IMG_SIZE),
                                                              batch_size=BATCH_SIZE,
                                                              class_mode='binary')
        # Dataset for testing
        test_data = ImageDataGenerator(rescale=1. / 255)
        self.test_set = test_data.flow_from_directory(TEST_PATH,
                                                         target_size=(IMG_SIZE, IMG_SIZE),
                                                         batch_size=BATCH_SIZE,
                                                         class_mode='binary')

    # Initialising the CNN
    def set(self):
        # Step 1 - Convolution
        self.add(Conv2D(32, (3, 3), input_shape=(IMG_SIZE, IMG_SIZE, 3),
                        activation='relu'))
        # Step 2 - Pooling
        self.add(MaxPooling2D(pool_size=(2, 2)))
        # Adding a second convolutional layer
        self.add(Conv2D(32, (3, 3), activation='relu'))
        self.add(MaxPooling2D(pool_size=(2, 2)))
        # Step 3 - Flattening
        self.add(Flatten())
        # Step 4 - Full connection
        self.add(Dense(units=128, activation='relu'))
        self.add(Dense(units=1, activation='sigmoid'))

    # Tran the CNN
    def tran(self):
        # Compiling the CNN
        self.compile(optimizer='adam', loss='binary_crossentropy',
                     metrics=['accuracy'])
        self.fit_generator(self.training_set,
                           steps_per_epoch=706,
                           epochs=EPOCHS,
                           validation_data=self.test_set,
                           validation_steps=2000,
                           verbose=2)


if __name__ == '__main__':
    model = Model()
    model.prepare_data()
    model.set()
    model.tran()
    mp = "./MODEL.h5"
    model.save(mp)
