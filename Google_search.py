pip install pytrends

import pandas as pd 
from pytrends.request import TrendReq 
import matplotlib.pyplot as plt 
Trending_topics = TrendReq(hl='en-US', tz=360)

kw_list=["Cloud Computing"] 
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')

Trending_topics.build_payload(kw_list=["Cloud Computing"], 
							cat=0, timeframe='today 12-m') 
data = Trending_topics.interest_over_time() 
data = data.sort_values(by="Cloud Computing", ascending = False) 
data = data.head(10) 
print(data)

kw_list = ["Cloud Computing"] 
Trending_topics.build_payload(kw_list) 
data = Trending_topics.get_historical_interest( 
kw_list, year_start=2018, month_start=1, day_start=1, 
hour_start=0, year_end=2018, month_end=2, day_end=1, 
hour_end=0, cat=0, geo='', gprop='', sleep=0) 
data = data.sort_values(by="Cloud Computing", ascending = False) 
data = data.head(10) 
print(data)

data = Trending_topics.interest_by_region() 
data = data.sort_values(by="Cloud Computing", 
						ascending = False) 
data = data.head(10) 
print(data)

data.reset_index().plot(x='geoName', y='Cloud Computing', 
						figsize=(10,5), kind="bar") 
plt.style.use('fivethirtyeight') 
plt.show()

df = Trending_topics.top_charts(2020, hl='en-US', 
								tz=300, geo='GLOBAL') 
df.head(10) 


Trending_topics.build_payload(kw_list=['Cloud Computing']) 
related_queries = Trending_topics.related_queries() 
related_queries.values()

keywords = Trending_topics.suggestions( 
keyword='Cloud Computing') 
df = pd.DataFrame(keywords) 
df.drop(columns= 'mid') 


