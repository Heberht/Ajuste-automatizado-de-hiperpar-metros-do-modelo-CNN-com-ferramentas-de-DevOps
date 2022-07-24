#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#For Convolution Layer which has number of Filters which help in Edge Detection
from keras.layers import Convolution2D


# In[ ]:


#for Pooling which Reduces the size of image using Strides 
from keras.layers import MaxPooling2D


# In[ ]:


#for Flatterneing the image to Convert it from 3D to 2D
from keras.layers import Flatten


# In[ ]:


#for Neural Ntwork
from keras.layers import Dense


# In[ ]:


#Model for Training 
from keras.models import Sequential


# In[ ]:


model = Sequential()


# In[ ]:


model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        strides=(1,1),
                        activation='relu',
                        input_shape=(250,250,3)))


# In[ ]:


model.add(MaxPooling2D(pool_size=(2,2)))


# In[ ]:


model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        activation='relu'))


# In[ ]:


model.add(MaxPooling2D(pool_size=(2,2)))


# In[ ]:


model.add(Flatten())


# In[ ]:


model.add(Dense(units=128,
                activation='relu'))


# In[ ]:


model.add(Dense(units=64,
               activation='relu'))


# In[ ]:


model.add(Dense(units=32,
               activation='relu'))


# In[ ]:


model.add(Dense(units=1,
               activation='sigmoid'))


# In[ ]:


from keras.optimizers import Adam


# In[ ]:


model.compile(optimizer=Adam(),
             loss='binary_crossentropy',
             metrics=['accuracy'])


# In[ ]:





# In[ ]:


from keras_preprocessing.image import ImageDataGenerator


# In[ ]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'C:/Users/a/Desktop/Jupytr/DL-NN/CNN/Face Recognization using CNN/Dataset/Data_Train/',
        target_size=(250, 250),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'C:/Users/a/Desktop/Jupytr/DL-NN/CNN/Face Recognization using CNN/Dataset/Data_Test/',
        target_size=(250, 250),
        batch_size=32,
        class_mode='binary')

model.fit(
        training_set,
        steps_per_epoch=2000,
        epochs=1,
        validation_data=test_set,
        validation_steps=800)


# In[ ]:


model.save('face_model.h5')


# In[ ]:


training_set.class_indices


# In[ ]:




