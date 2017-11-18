
# coding: utf-8

# In[1]:

import graphlabphlab


# In[2]:

people = graphlab.SFrame('people_wiki.gl/')


# # 1. Compare top words according to word counts to TF-IDF:

# In[3]:

people.head()


# In[5]:

people['word_count'] = graphlab.text_analytics.count_words(people['text'])
people.head()


# In[6]:

people['tfidf'] = graphlab.text_analytics.tf_idf(people['word_count'])
people.head()


# In[7]:

john = people[people['name'] =='Elton John']


# In[9]:

john_word_count_table = john[['word_count']].stack('word_count',new_column_name=['word','count'])
john_word_count_table.head()


# In[10]:

john_word_count_table.sort('count',ascending=False)


# In[13]:

john[['tfidf']].stack('tfidf',new_column_name=['word','tfidf']).sort('tfidf',ascending=False)


# # 2. Measuring distance:

# In[14]:

beckham = people[people['name'] == 'Victoria Beckham']


# In[16]:

paul = people[people['name'] == 'Paul McCartney']


# In[17]:

graphlab.distances.cosine(john['tfidf'][0],beckham['tfidf'][0])


# In[18]:

graphlab.distances.cosine(john['tfidf'][0],paul['tfidf'][0])


# # 3.Building nearest neighbors models with different input features and setting the distance metric:

# In[21]:

knn_tfidf_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name',distance='cosine')


# In[22]:

knn_wordcount_model = graphlab.nearest_neighbors.create(people,features=['word_count'],label='name',distance='cosine')


# In[24]:

knn_wordcount_model.query(john)


# In[25]:

knn_tfidf_model.query(john)


# In[26]:

knn_wordcount_model.query(beckham)


# In[27]:

knn_tfidf_model.query(beckham)


# In[ ]:



