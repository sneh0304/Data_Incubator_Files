from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

#Values were added manually from solr after indexing the tweets
hashtags = {"#coronalockdown":4011,
        "#coronavirus":2810,
        "#coronavirusoutbreak":1981,
        "#covid19":1735,
        "#coronaupdate":1673,
        "#coronavirusoutbreakindia":1495,
        "#animalcrossing":680,
        "#coronavirusindia":581,
        "#covid2019":532,
        "#covid":363,
        "#stayhome":334,
        "#corona":298,
        "#covid_19":274,
        "#lockdown":244,
        "#coronaviruspandemic":200,
        "#lockdownwithoutplan":175,
        "#coronavillains":160,
        "#stayhomestaysafe":160,
        "#21daylockdown":137,
        "#coronavirusupdate":129,
        "#indiafightscorona":125,
        "#coronaviruslockdown":119,
        "#staysafe":119,
        "#italy":113,
        "#lockdown21":104}
wordcloud = WordCloud(width = 800, height = 400, 
                background_color ='white',
                min_font_size = 15,
                colormap = "inferno").generate_from_frequencies(hashtags) 
                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud, interpolation = "bilinear") 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.savefig('hashtags_WC.png')
plt.show()

#Values were added manually from solr after indexing the tweets
tweet_ids = ['1243715384802529281', '1243728791324618752', '1243718733903941632', '1243561928196100097', '1243731802474201089', '1243601688314949636', '1243714254777151488', '1243712427067236352', '1243537928862797825', '1243734901997703170']
likes = [715, 354, 272, 197, 193, 170, 169, 164, 162, 126]
y_pos = np.arange(len(tweet_ids))

plt.figure(figsize = (8, 5))
plt.barh(y_pos, likes, align = 'center', alpha = 0.5)
plt.yticks(y_pos, tweet_ids)
plt.xlabel('Likes')
plt.title('Top 10 tweets with max likes')

plt.savefig('likes_barh.png')
plt.show()