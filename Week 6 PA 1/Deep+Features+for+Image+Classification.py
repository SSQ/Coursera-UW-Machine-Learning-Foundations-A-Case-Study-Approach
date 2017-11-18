
# coding: utf-8

# # Using deep features to build an image classifier
# 
# # Fire up GraphLab Create

# In[1]:

import graphlab


# # Load a common image analysis dataset
# 
# We will use a popular benchmark dataset in computer vision called CIFAR-10.  
# 
# (We've reduced the data to just 4 categories = {'cat','bird','automobile','dog'}.)
# 
# This dataset is already split into a training set and test set.  

# In[2]:

image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')


# # Exploring the image data

# In[3]:

graphlab.canvas.set_target('ipynb')


# In[4]:

image_train['image'].show()


# # Train a classifier on the raw image pixels
# 
# We first start by training a classifier on just the raw pixels of the image.

# In[5]:

raw_pixel_model = graphlab.logistic_classifier.create(image_train,target='label',
                                              features=['image_array'])


# # Make a prediction with the simple model based on raw pixels

# In[6]:

image_test[0:3]['image'].show()


# In[7]:

image_test[0:3]['label']


# In[8]:

raw_pixel_model.predict(image_test[0:3])


# The model makes wrong predictions for all three images.

# # Evaluating raw pixel model on test data

# In[9]:

raw_pixel_model.evaluate(image_test)


# The accuracy of this model is poor, getting only about 46% accuracy.

# # Can we improve the model using deep features
# 
# We only have 2005 data points, so it is not possible to train a deep neural network effectively with so little data.  Instead, we will use transfer learning: using deep features trained on the full ImageNet dataset, we will train a simple model on this small dataset.

# In[10]:

len(image_train)


# ## Computing deep features for our images
# 
# The two lines below allow us to compute deep features.  This computation takes a little while, so we have already computed them and saved the results as a column in the data you loaded. 
# 
# (Note that if you would like to compute such deep features and have a GPU on your machine, you should use the GPU enabled GraphLab Create, which will be significantly faster for this task.)

# In[11]:

#deep_learning_model = graphlab.load_model('http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45')
#image_train['deep_features'] = deep_learning_model.extract_features(image_train)


# As we can see, the column deep_features already contains the pre-computed deep features for this data. 

# In[12]:

image_train.head()


# # Given the deep features, let's train a classifier

# In[13]:

deep_features_model = graphlab.logistic_classifier.create(image_train,
                                                         features=['deep_features'],
                                                         target='label')


# # Apply the deep features model to first few images of test set

# In[14]:

image_test[0:3]['image'].show()


# In[15]:

deep_features_model.predict(image_test[0:3])


# The classifier with deep features gets all of these images right!

# # Compute test_data accuracy of deep_features_model
# 
# As we can see, deep features provide us with significantly better accuracy (about 78%)

# In[16]:

deep_features_model.evaluate(image_test)

