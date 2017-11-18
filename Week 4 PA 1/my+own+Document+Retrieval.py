
# coding: utf-8

# In[1]:

import graphlab


# # Load some text data - from wikipedia, pages on people

# In[2]:

people = graphlab.SFrame('people_wiki.gl/')


# In[3]:

people.head()


# In[4]:

len(people)


# # Explore the dataset and checkout the text it contains

# In[5]:

obama = people[people['name'] == 'Barack Obama']


# In[6]:

obama


# In[7]:

obama['text']


# In[8]:

clooney = people[people['name'] == 'George Clooney']
clooney['text']


# # Get the word counts for Obama article

# In[9]:

obama['word_count'] = graphlab.text_analytics.count_words(obama['text'])


# In[10]:

print obama['word_count']


# # Sort the word counts for the Obama article

# In[11]:

obama_word_count_table = obama[['word_count']].stack('word_count', new_column_name = ['word','count'])


# In[12]:

obama_word_count_table.head()


# In[13]:

obama_word_count_table.sort('count',ascending=False)


# # Compute TF-IDF for the corpus

# In[14]:

people['word_count'] = graphlab.text_analytics.count_words(people['text'])
people.head()


# In[15]:

tfidf = graphlab.text_analytics.tf_idf(people['word_count'])
tfidf


# In[16]:

people['tfidf'] = tfidf
print graphlab.version


# In[17]:

people.head()


# # Examine the TF-IDF for the Obama article

# In[18]:

obama = people[people['name'] == 'Barack Obama']


# In[19]:

obama[['tfidf']].stack('tfidf',new_column_name=['word','count']).sort('count',ascending=False)


# # Manually compute distances between a few people

# In[20]:

clinton = people[people['name'] == 'Bill Clinton']


# In[21]:

beckham = people[people['name'] == 'David Beckham']


# # Is Obama closer to Clinton than to Beckham?

# In[22]:

graphlab.distances.cosine(obama['tfidf'][0],clinton['tfidf'][0])


# In[23]:

graphlab.distances.cosine(obama['tfidf'][0],beckham['tfidf'][0])


# # Build a nearest neighbor model for document retrieval

# In[24]:

knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name')


# # Applying the nearest-neighbors model for retrieval

# ## Who is closest to Obama?

# In[25]:

knn_model.query(obama)


# # Other examples of document retrieval

# In[26]:

swift = people[people['name'] == 'Taylor Swift']


# In[27]:

knn_model.query(swift)


# In[28]:

jolie = people[people['name'] == 'Angelina Jolie']


# In[29]:

knn_model.query(jolie)


# In[30]:

arnold = people[people['name'] == 'Arnold Schwarzenegger']


# In[31]:

knn_model.query(arnold)


# In[ ]:



