import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(30))
views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views)

is_clicked = lambda x: True if x > 0 else False
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(is_clicked)
print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

view = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(view)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']


group_a = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
group_a_pivot = group_a.pivot(columns='day', index='is_click',values='user_id').reset_index()
print(group_a_pivot)

group_b = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
group_b_pivot = group_b.pivot(columns = 'day', index = 'is_click', values = 'user_id').reset_index()
print(group_b_pivot)

#I recommend using Group A as the true values always surpassed Group B values