

```python
import graphlab
```

# 1. Counting unique users:  'Kanye West', 'Foo Fighters', 'Taylor Swift' and 'Lady GaGa'


```python
song_data = graphlab.SFrame('song_data.gl/')
```


```python
song_data.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">listen_count</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">title</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOAKIMP12A8C130995</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Cove</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Jack Johnson</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBBMDR12A8C13253B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Entre Dos Aguas</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Paco De Lucia</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBXHDL12A81C204C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stronger</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Kanye West</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBYHAJ12A6701BF1D</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Constellations</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Jack Johnson</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODACBL12A8C13C273</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Learn To Fly</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Foo Fighters</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODDNQT12A6D4F5F7E</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Apuesta Por El Rock 'N'<br>Roll ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Héroes del Silencio</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODXRTY12AB0180F3B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Paper Gangsta</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lady GaGa</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFGUAY12AB017B0A8</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stacked Actors</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Foo Fighters</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFRQTD12A81C233C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sehr kosmisch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Harmonia</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOHQWYZ12A6D4FA701</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Heaven's gonna burn your<br>eyes ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Thievery Corporation<br>feat. Emiliana Torrini ...</td>
    </tr>
</table>
<table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Cove - Jack Johnson</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Entre Dos Aguas - Paco De<br>Lucia ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stronger - Kanye West</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Constellations - Jack<br>Johnson ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Learn To Fly - Foo<br>Fighters ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Apuesta Por El Rock 'N'<br>Roll - Héroes del ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Paper Gangsta - Lady GaGa</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stacked Actors - Foo<br>Fighters ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sehr kosmisch - Harmonia</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Heaven's gonna burn your<br>eyes - Thievery ...</td>
    </tr>
</table>
[10 rows x 6 columns]<br/>
</div>




```python
graphlab.canvas.set_target('ipynb')
```


```python
len(song_data[song_data['artist'] == 'Kanye West'].unique())
```




    3775




```python
len(song_data[song_data['artist'] == 'Foo Fighters'].unique())
```




    3429




```python
len(song_data[song_data['artist'] == 'Taylor Swift'].unique())
```




    6227




```python
len(song_data[song_data['artist'] == 'Lady GaGa'].unique())
```




    4129



# 2. Using groupby-aggregate to find the most popular and least popular artist:


```python
song_data_groupby = song_data.groupby(key_columns='artist', operations={'total_count': graphlab.aggregate.SUM('listen_count')})
song_data_groupby.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">total_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Dells</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">274</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lil Jon / The East Side<br>Boyz ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">197</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Tom Petty And The<br>Heartbreakers ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2867</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Blackstreet</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">747</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Ratatat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3727</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Shotta</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">82</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Airscape</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">130</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Mecano</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">172</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Moimir Papalescu &amp; The<br>Nihilists ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">177</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Brad Paisley</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2731</td>
    </tr>
</table>
[10 rows x 2 columns]<br/>
</div>




```python
song_data_groupby_de = song_data_groupby.sort('total_count',ascending=False)
song_data_groupby_de.head()
song_data_groupby_de[0]
```




    {'artist': 'Kings Of Leon', 'total_count': 43218L}




```python
song_data_groupby_as = song_data_groupby.sort('total_count',ascending=True)
song_data_groupby_as.head()
song_data_groupby_as[0]
```




    {'artist': 'William Tabbert', 'total_count': 14L}



 # 3. Using groupby-aggregate to find the most recommended songs:


```python
train_data,test_data = song_data.random_split(.8,seed=0)
```


```python
personalized_model = graphlab.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='song')
```


<pre>Recsys training: model = item_similarity</pre>



<pre>Warning: Ignoring columns song_id, listen_count, title, artist;</pre>



<pre>    To use one of these as a target column, set target = <column_name></pre>



<pre>    and use a method that allows the use of a target.</pre>



<pre>Preparing data set.</pre>



<pre>    Data has 893580 observations with 66085 users and 9952 items.</pre>



<pre>    Data prepared in: 1.28407s</pre>



<pre>Training model from provided data.</pre>



<pre>Gathering per-item and per-user statistics.</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| Elapsed Time (Item Statistics) | % Complete |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| 1ms                            | 1.5        |</pre>



<pre>| 27.002ms                       | 100        |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>Setting up lookup tables.</pre>



<pre>Processing data in one pass using dense lookup tables.</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| Elapsed Time (Constructing Lookups) | Total % Complete | Items Processed |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| 267.016ms                           | 0                | 0               |</pre>



<pre>| 1.79s                               | 100              | 9952            |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>Finalizing lookup tables.</pre>



<pre>Generating candidate set for working with new users.</pre>



<pre>Finished training in 2.88617s</pre>



```python
subset_test_users = test_data['user_id'].unique()[0:10000]
subset_test_users.head()
```




    dtype: str
    Rows: 10
    ['c66c10a9567f0d82ff31441a9fd5063e5cd9dfe8', 'c067c22072a17d33310d7223d7b79f819e48cf42', 'f6c596a519698c97f1591ad89f540d76f6a04f1a', '696787172dd3f5169dc94deef97e427cee86147d', '3a7111f4cdf3c5a85fd4053e3cc2333562e1e0cb', '532e98155cbfd1e1a474a28ed96e59e50f7c5baf', 'ee43b175ed753b2e2bce806c903d4661ad351a91', 'e372c27f6cb071518ae500589ae02c126954c148', '83b1428917b47a6b130ed471b09033820be78a8c', '39487deef9345b1e22881245cabf4e7c53b6cf6e']




```python
personalized_model_recommend = personalized_model.recommend(subset_test_users,k=1)
personalized_model_recommend.head()
```


<pre>recommendations finished on 1000/10000 queries. users per second: 9258.74</pre>



<pre>recommendations finished on 2000/10000 queries. users per second: 10637.7</pre>



<pre>recommendations finished on 3000/10000 queries. users per second: 11449.7</pre>



<pre>recommendations finished on 4000/10000 queries. users per second: 11833.7</pre>



<pre>recommendations finished on 5000/10000 queries. users per second: 12135.2</pre>



<pre>recommendations finished on 6000/10000 queries. users per second: 12319.6</pre>



<pre>recommendations finished on 7000/10000 queries. users per second: 12454.8</pre>



<pre>recommendations finished on 8000/10000 queries. users per second: 12717.9</pre>



<pre>recommendations finished on 9000/10000 queries. users per second: 12311.2</pre>



<pre>recommendations finished on 10000/10000 queries. users per second: 11049.1</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">score</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">c66c10a9567f0d82ff31441a9<br>fd5063e5cd9dfe8 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Cuando Pase El Temblor -<br>Soda Stereo ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0194504536115</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">c067c22072a17d33310d7223d<br>7b79f819e48cf42 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Grind With Me (Explicit<br>Version) - Pretty Ricky ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0459424376488</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">f6c596a519698c97f1591ad89<br>f540d76f6a04f1a ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Hey_ Soul Sister - Train</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0238929539919</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">696787172dd3f5169dc94deef<br>97e427cee86147d ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Senza Una Donna (Without<br>A Woman) - Zucchero / ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.017026577677</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3a7111f4cdf3c5a85fd4053e3<br>cc2333562e1e0cb ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Heartbreak Warfare - John<br>Mayer ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0298416515191</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">532e98155cbfd1e1a474a28ed<br>96e59e50f7c5baf ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Jive Talkin' (Album<br>Version) - Bee Gees ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0118288653237</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">ee43b175ed753b2e2bce806c9<br>03d4661ad351a91 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Ricordati Di Noi -<br>Valerio Scanu ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0305171211561</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">e372c27f6cb071518ae500589<br>ae02c126954c148 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Fall Out - The Police</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0819672048092</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">83b1428917b47a6b130ed471b<br>09033820be78a8c ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Clocks - Coldplay</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0440290331841</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39487deef9345b1e22881245c<br>abf4e7c53b6cf6e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Black Mirror - Arcade<br>Fire ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0417737685717</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
</table>
[10 rows x 4 columns]<br/>
</div>




```python
personalized_model_recommend_groupby = personalized_model_recommend.groupby(key_columns='song',operations={'count': graphlab.aggregate.COUNT()})
personalized_model_recommend_groupby.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Climb - Miley Cyrus</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Hey Daddy (Daddy's Home)<br>- Usher ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I Gotta Feeling - Black<br>Eyed Peas ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">17</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Cerdo - Molotov</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Ich Will - Rammstein</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">9</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Too Deep - Girl Talk</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Dumpweed - Blink-182</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Guys Like Me - Eric<br>Church ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I Can't Love You Back -<br>Easton Corbin ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Freedom - Akon</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
</table>
[10 rows x 2 columns]<br/>
</div>




```python
personalized_model_recommend_groupby_de = personalized_model_recommend_groupby.sort('count',ascending=False)
personalized_model_recommend_groupby_de.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Undo - Björk</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">439</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Secrets - OneRepublic</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">383</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Revelry - Kings Of Leon</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">223</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">You're The One - Dwight<br>Yoakam ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">165</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Fireflies - Charttraxx<br>Karaoke ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">120</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sehr kosmisch - Harmonia</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">99</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Horn Concerto No. 4 in E<br>flat K495: II. Romance ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">93</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Hey_ Soul Sister - Train</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">91</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">OMG - Usher featuring<br>will.i.am ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">61</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Dog Days Are Over (Radio<br>Edit) - Florence + The ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">47</td>
    </tr>
</table>
[10 rows x 2 columns]<br/>
</div>




```python

```
