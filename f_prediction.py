#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.models import load_model


# In[ ]:


model = load_model('face_model.h5')


# In[ ]:


model.summary()


# In[ ]:


from keras.preprocessing import image


# In[ ]:


test_img = image.load_img('C:/Users/a/Desktop/Jupytr/DL-NN/CNN/Face Recognization using CNN/Test_img/lol1.jpg', target_size=(250,250))


# In[ ]:


type(test_img)


# In[ ]:


test_img


# In[ ]:


image.img_to_array(test_img)


# In[ ]:


import numpy as np


# In[ ]:


test_img = np.expand_dims(test_img, axis=0)


# In[ ]:


type(test_img)


# In[ ]:


test_img.shape


# In[ ]:


result = model.predict(test_img)


# In[ ]:


print(result)


# In[ ]:


if result[0][0]==0:
    print('Naman')
else:
    print('Soumyata')


# In[ ]:




