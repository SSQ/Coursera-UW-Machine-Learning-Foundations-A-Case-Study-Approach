

```python
import graphlab
```

# 1.Computing summary statistics of the data:   bird 


```python
image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')
```

    [INFO] graphlab.cython.cy_server: GraphLab Create v2.1 started. Logging: C:\Users\Beginner\AppData\Local\Temp\graphlab_server_1477826376.log.0
    

    This non-commercial license of GraphLab Create for academic use is assigned to ssq6554@gmail.com and will expire on October 10, 2017.
    


```python
graphlab.canvas.set_target('ipynb')
```


```python
image_train.show()
```




```python
image_train.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">deep_features</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image_array</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">24</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.242871761322,<br>1.09545373917, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[73.0, 77.0, 58.0, 71.0,<br>68.0, 50.0, 77.0, 69.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">33</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.525087952614, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[7.0, 5.0, 8.0, 7.0, 5.0,<br>8.0, 5.0, 4.0, 6.0, 7.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.566015958786, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[169.0, 122.0, 65.0,<br>131.0, 108.0, 75.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">70</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.12979578972, 0.0, 0.0,<br>0.778194487095, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[154.0, 179.0, 152.0,<br>159.0, 183.0, 157.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">90</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.71786928177, 0.0, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[216.0, 195.0, 180.0,<br>201.0, 178.0, 160.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">97</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">automobile</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.57818555832, 0.0, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[33.0, 44.0, 27.0, 29.0,<br>44.0, 31.0, 32.0, 45.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">107</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0,<br>0.220677852631, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[97.0, 51.0, 31.0, 104.0,<br>58.0, 38.0, 107.0, 61.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">121</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.23753464222, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[93.0, 96.0, 88.0, 102.0,<br>106.0, 97.0, 117.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">136</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">automobile</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0, 0.0, 0.0, 0.0,<br>0.0, 7.5737862587, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[35.0, 59.0, 53.0, 36.0,<br>56.0, 56.0, 42.0, 62.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">138</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.658935725689, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[205.0, 193.0, 195.0,<br>200.0, 187.0, 193.0, ...</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>




```python
image_train['label'].head()
```




    dtype: str
    Rows: 10
    ['bird', 'cat', 'cat', 'dog', 'bird', 'automobile', 'dog', 'bird', 'automobile', 'bird']




```python
image_train['label'].sketch_summary()
```




    
    +------------------+-------+----------+
    |       item       | value | is exact |
    +------------------+-------+----------+
    |      Length      |  2005 |   Yes    |
    | # Missing Values |   0   |   Yes    |
    | # unique values  |   4   |    No    |
    +------------------+-------+----------+
    
    Most frequent items:
    +-------+------------+-----+-----+------+
    | value | automobile | cat | dog | bird |
    +-------+------------+-----+-----+------+
    | count |    509     | 509 | 509 | 478  |
    +-------+------------+-----+-----+------+
    



# 2. Creating category-specific image retrieval models: 16289, 16976


```python
dog_train_data = image_train[image_train['label']=='dog']
```


```python
len(dog_train_data)
```




    509




```python
dog_train_data.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">deep_features</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image_array</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">70</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.12979578972, 0.0, 0.0,<br>0.778194487095, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[154.0, 179.0, 152.0,<br>159.0, 183.0, 157.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">107</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0,<br>0.220677852631, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[97.0, 51.0, 31.0, 104.0,<br>58.0, 38.0, 107.0, 61.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">177</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 1.45965671539, 0.0,<br>0.422992348671, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[55.0, 75.0, 42.0, 51.0,<br>76.0, 37.0, 57.0, 83.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">424</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.942399680614, 0.0,<br>0.220352768898, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[60.0, 35.0, 18.0, 63.0,<br>49.0, 38.0, 66.0, 56.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">462</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.43462562561, 0.0, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[86.0, 69.0, 75.0, 57.0,<br>41.0, 48.0, 46.0, 35.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">542</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.451547086239, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[196.0, 174.0, 113.0,<br>140.0, 117.0, 65.0, 8 ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">573</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.592360973358, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[153.0, 103.0, 52.0,<br>151.0, 102.0, 49.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">851</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.690123438835, 0.0,<br>0.0, 0.0, 0.305860161 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[39.0, 6.0, 4.0, 53.0,<br>23.0, 24.0, 57.0, 37.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">919</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.177558660507,<br>0.139396846294, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[29.0, 43.0, 4.0, 24.0,<br>35.0, 6.0, 24.0, 37.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1172</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.517601490021, 0.0,<br>1.96418333054, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[182.0, 180.0, 197.0,<br>196.0, 192.0, 209.0, ...</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>




```python
cat_train_data = image_train[image_train['label']=='cat']
automobile_train_data = image_train[image_train['label']=='automobile']
bird_train_data = image_train[image_train['label']=='bird']
```


```python
dog_model = graphlab.nearest_neighbors.create(dog_train_data,features=['deep_features'],
                                             label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



```python
cat_model = graphlab.nearest_neighbors.create(cat_train_data,features=['deep_features'],
                                             label='id')
automobile_model = graphlab.nearest_neighbors.create(automobile_train_data,features=['deep_features'],
                                             label='id')
bird_model = graphlab.nearest_neighbors.create(bird_train_data,features=['deep_features'],
                                             label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Starting brute force nearest neighbors model training.</pre>



```python
cat = image_test[0:1]
```


```python
cat['image'].show()
```




```python
cat_model.query(cat)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 7ms          |</pre>



<pre>| Done         |         | 100         | 103.006ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">query_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">reference_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">distance</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">16289</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.623719208</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45646</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.0068799284</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">32139</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.5200813436</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">25713</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.7548502521</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">331</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.8731228168</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')
```


```python
cat_neighbors = get_images_from_ids(cat_model.query(cat))
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 5ms          |</pre>



<pre>| Done         |         | 100         | 104.006ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
cat_neighbors['image'].show()
```




```python
dog_model.query(cat)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 8ms          |</pre>



<pre>| Done         |         | 100         | 107.006ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">query_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">reference_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">distance</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">16976</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.4642628784</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">13387</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.5666832169</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">35867</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.6047267079</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">44603</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.7065585153</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">6094</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.5113254907</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
get_images_from_ids(dog_model.query(cat))['image'].show()
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 8.001ms      |</pre>



<pre>| Done         |         | 100         | 87.005ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>




# 3. A simple example of nearest-neighbors classification: 36.15573070978294, 37.77071136184156,


```python
cat_model.query(cat)['distance'].mean()
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 6.001ms      |</pre>



<pre>| Done         |         | 100         | 141.008ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>





    36.15573070978294




```python
dog_model.query(cat)['distance'].mean()
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 7ms          |</pre>



<pre>| Done         |         | 100         | 93.005ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>





    37.77071136184156



# 4. [Challenging Question] Computing nearest neighbors accuracy using SFrame operations: 


```python
image_test_dog = image_test[image_test['label']=='dog']
image_test_cat = image_test[image_test['label']=='cat']
image_test_automobile = image_test[image_test['label']=='automobile']
image_test_bird = image_test[image_test['label']=='bird']
```


```python
dog_cat_neighbors = cat_model.query(image_test_dog, k=1)
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 4</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 128000  | 25.1473     | 484.027ms    |</pre>



<pre>| Done         | 509000  | 100         | 696.039ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_dog_neighbors = dog_model.query(image_test_dog, k=1)
dog_automobile_neighbors = automobile_model.query(image_test_dog, k=1)
dog_bird_neighbors = bird_model.query(image_test_dog, k=1)
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 4</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 127000  | 24.9509     | 481.027ms    |</pre>



<pre>| Done         | 509000  | 100         | 675.038ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 4</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 127000  | 24.9509     | 557.031ms    |</pre>



<pre>| Done         | 509000  | 100         | 728.041ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 4</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 120000  | 25.1046     | 500.029ms    |</pre>



<pre>| Done         | 478000  | 100         | 733.042ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_distances = graphlab.SFrame({'dog-automobile': dog_automobile_neighbors['distance'],
                                 'dog-bird': dog_bird_neighbors['distance'],
                                 'dog-cat': dog_cat_neighbors['distance'],
                                 'dog-dog': dog_dog_neighbors['distance']})
```


```python
dog_distances.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-automobile</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-bird</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-cat</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-dog</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.9579761457</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.7538647304</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.4196077068</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">33.4773590373</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">46.0021331807</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.3382958925</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.8353268874</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">32.8458495684</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">42.9462290692</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.6157590853</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.9763410854</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">35.0397073189</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.6866060048</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.0892269954</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.5750072914</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">33.9010327697</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.2269664935</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.272288694</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.778824791</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.4849250909</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">40.5845117698</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.1462089236</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">35.1171578292</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.945165344</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45.1067352961</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">40.523040106</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">40.6095830913</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.0957278345</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.3221140974</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.1947918393</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.9036867306</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.7696131032</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.8244654995</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">40.1567131661</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.0674700168</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">35.1089144603</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45.4976929401</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45.5597962603</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">42.7258732951</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">43.2422832585</td>
    </tr>
</table>
[10 rows x 4 columns]<br/>
</div>



## Computing the number of correct predictions using 1-nearest neighbors for the dog class: 


```python
def is_dog_correct(row):
    return (row['dog-dog'] < row['dog-automobile']) & (row['dog-dog'] < row['dog-bird']) & (row['dog-dog'] < row['dog-cat'])
    
```


```python
dog_distances.apply(is_dog_correct)
```




    dtype: int
    Rows: 1000
    [1L, 1L, 1L, 1L, 0L, 1L, 1L, 1L, 1L, 0L, 1L, 0L, 0L, 1L, 1L, 1L, 1L, 0L, 0L, 1L, 0L, 0L, 0L, 0L, 1L, 1L, 0L, 1L, 1L, 0L, 1L, 1L, 0L, 1L, 1L, 1L, 1L, 1L, 0L, 0L, 1L, 1L, 0L, 1L, 1L, 0L, 1L, 1L, 1L, 1L, 0L, 0L, 1L, 1L, 0L, 1L, 1L, 1L, 0L, 0L, 1L, 0L, 0L, 1L, 0L, 1L, 0L, 0L, 0L, 1L, 1L, 1L, 1L, 0L, 0L, 0L, 1L, 1L, 1L, 1L, 1L, 1L, 0L, 0L, 1L, 1L, 1L, 1L, 1L, 1L, 1L, 0L, 1L, 1L, 1L, 1L, 1L, 1L, 0L, 0L, ... ]




```python
dog_distances.apply(is_dog_correct).sum()
```




    678L




```python

```
