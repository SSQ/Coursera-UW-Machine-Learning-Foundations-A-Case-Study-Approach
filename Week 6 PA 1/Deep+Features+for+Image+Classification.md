
# Using deep features to build an image classifier

# Fire up GraphLab Create


```python
import graphlab
```

# Load a common image analysis dataset

We will use a popular benchmark dataset in computer vision called CIFAR-10.  

(We've reduced the data to just 4 categories = {'cat','bird','automobile','dog'}.)

This dataset is already split into a training set and test set.  


```python
image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')
```

    [INFO] This commercial license of GraphLab Create is assigned to engr@dato.com.
    
    [INFO] Start server at: ipc:///tmp/graphlab_server-123075 - Server binary: /home/ubuntu/anaconda/lib/python2.7/site-packages/graphlab/unity_server - Server log: /tmp/graphlab_server_1440701433.log
    [INFO] GraphLab Server Version: 1.5.2
    

# Exploring the image data


```python
graphlab.canvas.set_target('ipynb')
```


```python
image_train['image'].show()
```



# Train a classifier on the raw image pixels

We first start by training a classifier on just the raw pixels of the image.


```python
raw_pixel_model = graphlab.logistic_classifier.create(image_train,target='label',
                                              features=['image_array'])
```

    PROGRESS: Creating a validation set from 5 percent of training data. This may take a while.
              You can set ``validation_set=None`` to disable validation tracking.
    
    PROGRESS: Logistic regression:
    PROGRESS: --------------------------------------------------------
    PROGRESS: Number of examples          : 1900
    PROGRESS: Number of classes           : 4
    PROGRESS: Number of feature columns   : 1
    PROGRESS: Number of unpacked features : 3072
    PROGRESS: Number of coefficients    : 9219
    PROGRESS: Starting L-BFGS
    PROGRESS: --------------------------------------------------------
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    PROGRESS: | Iteration | Passes   | Step size | Elapsed Time | Training-accuracy | Validation-accuracy |
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    PROGRESS: | 1         | 6        | 0.000013  | 1.298911     | 0.280526          | 0.276190            |
    PROGRESS: | 2         | 8        | 1.000000  | 1.426180     | 0.364211          | 0.314286            |
    PROGRESS: | 3         | 9        | 1.000000  | 1.499995     | 0.411579          | 0.409524            |
    PROGRESS: | 4         | 10       | 1.000000  | 1.577665     | 0.435263          | 0.514286            |
    PROGRESS: | 5         | 11       | 1.000000  | 1.653563     | 0.464211          | 0.533333            |
    PROGRESS: | 6         | 12       | 1.000000  | 1.727710     | 0.467368          | 0.523810            |
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    

# Make a prediction with the simple model based on raw pixels


```python
image_test[0:3]['image'].show()
```




```python
image_test[0:3]['label']
```




    dtype: str
    Rows: 3
    ['cat', 'automobile', 'cat']




```python
raw_pixel_model.predict(image_test[0:3])
```




    dtype: str
    Rows: 3
    ['bird', 'cat', 'bird']



The model makes wrong predictions for all three images.

# Evaluating raw pixel model on test data


```python
raw_pixel_model.evaluate(image_test)
```




    {'accuracy': 0.48025, 'confusion_matrix': Columns:
     	target_label	int
     	predicted_label	int
     	count	int
     
     Rows: 16
     
     Data:
     +--------------+-----------------+-------+
     | target_label | predicted_label | count |
     +--------------+-----------------+-------+
     |      2       |        0        |  148  |
     |      3       |        3        |  408  |
     |      1       |        2        |  168  |
     |      1       |        1        |  536  |
     |      2       |        3        |  276  |
     |      0       |        3        |  107  |
     |      2       |        1        |  217  |
     |      0       |        2        |  157  |
     |      0       |        1        |  118  |
     |      0       |        0        |  618  |
     +--------------+-----------------+-------+
     [16 rows x 3 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.}



The accuracy of this model is poor, getting only about 46% accuracy.

# Can we improve the model using deep features

We only have 2005 data points, so it is not possible to train a deep neural network effectively with so little data.  Instead, we will use transfer learning: using deep features trained on the full ImageNet dataset, we will train a simple model on this small dataset.


```python
len(image_train)
```




    2005



## Computing deep features for our images

The two lines below allow us to compute deep features.  This computation takes a little while, so we have already computed them and saved the results as a column in the data you loaded. 

(Note that if you would like to compute such deep features and have a GPU on your machine, you should use the GPU enabled GraphLab Create, which will be significantly faster for this task.)


```python
#deep_learning_model = graphlab.load_model('http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45')
#image_train['deep_features'] = deep_learning_model.extract_features(image_train)
```

As we can see, the column deep_features already contains the pre-computed deep features for this data. 


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



# Given the deep features, let's train a classifier


```python
deep_features_model = graphlab.logistic_classifier.create(image_train,
                                                         features=['deep_features'],
                                                         target='label')
```

    PROGRESS: Creating a validation set from 5 percent of training data. This may take a while.
              You can set ``validation_set=None`` to disable validation tracking.
    
    PROGRESS: WARNING: Detected extremely low variance for feature(s) 'deep_features' because all entries are nearly the same.
    Proceeding with model training using all features. If the model does not provide results of adequate quality, exclude the above mentioned feature(s) from the input dataset.
    PROGRESS: Logistic regression:
    PROGRESS: --------------------------------------------------------
    PROGRESS: Number of examples          : 1919
    PROGRESS: Number of classes           : 4
    PROGRESS: Number of feature columns   : 1
    PROGRESS: Number of unpacked features : 4096
    PROGRESS: Number of coefficients    : 12291
    PROGRESS: Starting L-BFGS
    PROGRESS: --------------------------------------------------------
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    PROGRESS: | Iteration | Passes   | Step size | Elapsed Time | Training-accuracy | Validation-accuracy |
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    PROGRESS: | 1         | 5        | 0.000130  | 0.376212     | 0.720688          | 0.732558            |
    PROGRESS: | 2         | 9        | 0.250000  | 0.717980     | 0.766024          | 0.790698            |
    PROGRESS: | 3         | 10       | 0.250000  | 0.892061     | 0.769151          | 0.802326            |
    PROGRESS: | 4         | 11       | 0.250000  | 1.022422     | 0.774883          | 0.802326            |
    PROGRESS: | 5         | 12       | 0.250000  | 1.152027     | 0.788431          | 0.802326            |
    PROGRESS: | 6         | 13       | 0.250000  | 1.287902     | 0.797290          | 0.790698            |
    PROGRESS: | 10        | 17       | 0.250000  | 1.812273     | 0.875456          | 0.767442            |
    PROGRESS: +-----------+----------+-----------+--------------+-------------------+---------------------+
    

# Apply the deep features model to first few images of test set


```python
image_test[0:3]['image'].show()
```




```python
deep_features_model.predict(image_test[0:3])
```




    dtype: str
    Rows: 3
    ['cat', 'automobile', 'cat']



The classifier with deep features gets all of these images right!

# Compute test_data accuracy of deep_features_model

As we can see, deep features provide us with significantly better accuracy (about 78%)


```python
deep_features_model.evaluate(image_test)
```




    {'accuracy': 0.788, 'confusion_matrix': Columns:
     	target_label	int
     	predicted_label	int
     	count	int
     
     Rows: 16
     
     Data:
     +--------------+-----------------+-------+
     | target_label | predicted_label | count |
     +--------------+-----------------+-------+
     |      0       |        2        |   12  |
     |      2       |        0        |   39  |
     |      1       |        2        |  115  |
     |      3       |        3        |  735  |
     |      1       |        3        |   66  |
     |      3       |        2        |  206  |
     |      0       |        3        |   7   |
     |      2       |        1        |   66  |
     |      0       |        1        |   20  |
     |      0       |        0        |  961  |
     +--------------+-----------------+-------+
     [16 rows x 3 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.}


