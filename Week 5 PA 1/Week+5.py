
# coding: utf-8

# In[14]:

import graphlab


# # 1. Counting unique users:  'Kanye West', 'Foo Fighters', 'Taylor Swift' and 'Lady GaGa'

# In[15]:

song_data = graphlab.SFrame('song_data.gl/')


# In[16]:

song_data.head()


# In[17]:

graphlab.canvas.set_target('ipynb')


# In[23]:

len(song_data[song_data['artist'] == 'Kanye West'].unique())


# In[24]:

len(song_data[song_data['artist'] == 'Foo Fighters'].unique())


# In[27]:

len(song_data[song_data['artist'] == 'Taylor Swift'].unique())


# In[28]:

len(song_data[song_data['artist'] == 'Lady GaGa'].unique())


# # 2. Using groupby-aggregate to find the most popular and least popular artist:

# In[39]:

song_data_groupby = song_data.groupby(key_columns='artist', operations={'total_count': graphlab.aggregate.SUM('listen_count')})
song_data_groupby.head()


# In[43]:

song_data_groupby_de = song_data_groupby.sort('total_count',ascending=False)
song_data_groupby_de.head()
song_data_groupby_de[0]


# In[41]:

song_data_groupby_as = song_data_groupby.sort('total_count',ascending=True)
song_data_groupby_as.head()
song_data_groupby_as[0]


#  # 3. Using groupby-aggregate to find the most recommended songs:

# In[44]:

train_data,test_data = song_data.random_split(.8,seed=0)


# In[45]:

personalized_model = graphlab.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='song')


# In[47]:

subset_test_users = test_data['user_id'].unique()[0:10000]
subset_test_users.head()


# In[49]:

personalized_model_recommend = personalized_model.recommend(subset_test_users,k=1)
personalized_model_recommend.head()


# In[50]:

personalized_model_recommend_groupby = personalized_model_recommend.groupby(key_columns='song',operations={'count': graphlab.aggregate.COUNT()})
personalized_model_recommend_groupby.head()


# In[51]:

personalized_model_recommend_groupby_de = personalized_model_recommend_groupby.sort('count',ascending=False)
personalized_model_recommend_groupby_de.head()


# In[ ]:



