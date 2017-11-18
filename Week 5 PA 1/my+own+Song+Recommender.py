
# coding: utf-8

# In[1]:

import graphlab


# # Load music data

# In[2]:

song_data = graphlab.SFrame('song_data.gl/')


# # Explore data

# In[3]:

song_data.head()


# In[4]:

graphlab.canvas.set_target('ipynb')


# In[5]:

song_data['song'].show()


# In[6]:

len(song_data)


# # count number of users

# In[8]:

users = song_data['user_id'].unique()


# In[9]:

len(users)


# # create a song recommender

# In[10]:

train_data,test_data = song_data.random_split(.8,seed=0)


# ## Simple popularity-based recommender

# In[25]:

popularity_model = graphlab.popularity_recommender.create(train_data,
                                                         user_id='user_id',
                                                         item_id='song')


# ### Use the popularity model to make some predictions

# In[26]:

popularity_model.recommend(users=[users[0]])


# In[27]:

popularity_model.recommend(users=[users[1]])


# In[28]:

popularity_model.recommend(users=[users[0],users[1]])


# ## Build a song recommender with personalization

# In[29]:

personalized_model = graphlab.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='song')


# ### Applying the personalized model to make song recommendations

# In[30]:

personalized_model.recommend(users=[users[0]])


# In[31]:

personalized_model.recommend(users=[users[1]])


# In[32]:

personalized_model.recommend(users=[users[2]])


# In[33]:

personalized_model.get_similar_items(['With Or Without You - U2'])


# In[34]:

personalized_model.get_similar_items(['Chan Chan (Live) - Buena Vista Social Club'])


# # Quantitative comparison between the models

# In[36]:

model_performance = graphlab.compare(test_data, [popularity_model, personalized_model], user_sample=0.05)
graphlab.show_comparison(model_performance,[popularity_model, personalized_model])


# In[ ]:



