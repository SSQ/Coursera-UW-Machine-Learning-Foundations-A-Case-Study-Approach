
# coding: utf-8

# In[1]:

import graphlab


# # 1.Computing summary statistics of the data:   bird 

# In[2]:

image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')


# In[6]:

graphlab.canvas.set_target('ipynb')


# In[7]:

image_train.show()


# In[8]:

image_train.head()


# In[9]:

image_train['label'].head()


# In[11]:

image_train['label'].sketch_summary()


# # 2. Creating category-specific image retrieval models: 16289, 16976

# In[29]:

dog_train_data = image_train[image_train['label']=='dog']


# In[30]:

len(dog_train_data)


# In[32]:

dog_train_data.head()


# In[33]:

cat_train_data = image_train[image_train['label']=='cat']
automobile_train_data = image_train[image_train['label']=='automobile']
bird_train_data = image_train[image_train['label']=='bird']


# In[34]:

dog_model = graphlab.nearest_neighbors.create(dog_train_data,features=['deep_features'],
                                             label='id')


# In[35]:

cat_model = graphlab.nearest_neighbors.create(cat_train_data,features=['deep_features'],
                                             label='id')
automobile_model = graphlab.nearest_neighbors.create(automobile_train_data,features=['deep_features'],
                                             label='id')
bird_model = graphlab.nearest_neighbors.create(bird_train_data,features=['deep_features'],
                                             label='id')


# In[36]:

cat = image_test[0:1]


# In[37]:

cat['image'].show()


# In[38]:

cat_model.query(cat)


# In[39]:

def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')


# In[40]:

cat_neighbors = get_images_from_ids(cat_model.query(cat))


# In[41]:

cat_neighbors['image'].show()


# In[42]:

dog_model.query(cat)


# In[43]:

get_images_from_ids(dog_model.query(cat))['image'].show()


# # 3. A simple example of nearest-neighbors classification: 36.15573070978294, 37.77071136184156,

# In[49]:

cat_model.query(cat)['distance'].mean()


# In[50]:

dog_model.query(cat)['distance'].mean()


# # 4. [Challenging Question] Computing nearest neighbors accuracy using SFrame operations: 

# In[53]:

image_test_dog = image_test[image_test['label']=='dog']
image_test_cat = image_test[image_test['label']=='cat']
image_test_automobile = image_test[image_test['label']=='automobile']
image_test_bird = image_test[image_test['label']=='bird']


# In[54]:

dog_cat_neighbors = cat_model.query(image_test_dog, k=1)


# In[59]:

dog_dog_neighbors = dog_model.query(image_test_dog, k=1)
dog_automobile_neighbors = automobile_model.query(image_test_dog, k=1)
dog_bird_neighbors = bird_model.query(image_test_dog, k=1)


# In[61]:

dog_distances = graphlab.SFrame({'dog-automobile': dog_automobile_neighbors['distance'],
                                 'dog-bird': dog_bird_neighbors['distance'],
                                 'dog-cat': dog_cat_neighbors['distance'],
                                 'dog-dog': dog_dog_neighbors['distance']})


# In[62]:

dog_distances.head()


# ## Computing the number of correct predictions using 1-nearest neighbors for the dog class: 

# In[71]:

def is_dog_correct(row):
    return (row['dog-dog'] < row['dog-automobile']) & (row['dog-dog'] < row['dog-bird']) & (row['dog-dog'] < row['dog-cat'])
    


# In[72]:

dog_distances.apply(is_dog_correct)


# In[73]:

dog_distances.apply(is_dog_correct).sum()


# In[ ]:



