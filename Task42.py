import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('C:\\Users\\HP\\Downloads\\USvideos.csv')

print(df.head())

print(df.shape)

df = df.drop_duplicates()
print(df.shape)

print(df.describe())

print(df.info)

columns_to_remove=['thumbnail_link','description']
df = df.drop(columns=columns_to_remove)
df.info()

from datetime import datetime
import datetime 

df["trending_date"] = df["trending_date"].apply(lambda x : datetime.datetime.strptime(x,'%y.%d.%m'))
print(df.head(3))

df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df.head(2))

df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.hour
df.head(2)

print(sorted(df["category_id"].unique()))
[1, 2, 10, 15, 17, 19, 20, 222, 23, 24, 25, 26, 27, 28, 29, 30, 43]

df['category_name'] = np.nan
df.loc[(df["category_id"] == 1), "category_name"] = 'File and Animation'
df.loc[(df["category_id"] == 2), "category_name"] = 'Autos and vehicles'
df.loc[(df["category_id"] == 10), "category_name"] = 'Music'
df.loc[(df["category_id"] == 15), "category_name"] = 'Pets and Animals'
df.loc[(df["category_id"] == 17), "category_name"] = 'Sports'
df.loc[(df["category_id"] == 19), "category_name"] = 'Travela and Events'
df.loc[(df["category_id"] == 20), "category_name"] = 'Gaming'
df.loc[(df["category_id"] == 22), "category_name"] = 'People and Blogs'
df.loc[(df["category_id"] == 23), "category_name"] = 'Comedy'
df.loc[(df["category_id"] == 24), "category_name"] = 'Entertainment'
df.loc[(df["category_id"] == 25), "category_name"] = 'News and Politics'
df.loc[(df["category_id"] == 26), "category_name"] = 'How to and Style'
df.loc[(df["category_id"] == 27), "category_name"] = 'Education'
df.loc[(df["category_id"] == 28), "category_name"] = 'Science and Technolgy'
df.loc[(df["category_id"] == 29), "category_name"] = 'Non Profit and Activism'
df.loc[(df["category_id"] == 30), "category_name"] = 'Movies'
df.loc[(df["category_id"] == 43), "category_name"] = 'Shows'

print(df.head())

df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby('year')['video_id'].count()

#create a bar chart
yearly_counts.plot(kind = 'bar', xlabel='Year', ylabel='Total Publish count', title='Total publish Video Per Year')

#show the chart 
plt.show()

#Group the data by 'category_name' and calculate the sum of 'views' in each category
category_views = df.groupby('category_name')['views'].sum().reset_index()

#Sort the categories by views in descending order
top_categories = category_views.sort_values(by='views',ascending=False).head(5)

#create a bar plot to visualize the top 5 categories
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name',fontsize=12)
plt.ylabel('Total Views',fontsize=12)
plt.title('Top 5 Categories',fontsize=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x= 'category_name', data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()

#count the number of videos publish per hour
video_per_hour = df['publish_hour'].value_counts().sort_index()
#create a bar plot
plt.figure(figsize=(12,6))
sns.barplot(x=video_per_hour.index, y=video_per_hour.values, palette='rocket')
plt.title('NUmber of Videos Publish per hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()


df['publish_time']=pd.to_datetime(df['publish_time'])
df['publish_date']=df['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()
plt.figure(figsize=(12,6))
sns.lineplot(data=video_count_by_date)
plt.title('Video Publish Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()


#Scatter plot between views and likes
sns.scatterplot(data=df, x='views', y='likes')
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

#Count plot
plt.figure(figsize = (14,8))
plt.subplots_adjust(wspace=0.2, hspace=0.4,top=0.9)
plt.subplot(2,2,1)
g= sns.countplot(x='comments_disabled', data=df)
g.set_title("Comments Disable", fontsize=16)
plt.subplot(2,2,2)
g1= sns.countplot(x='ratings_disabled', data=df)
g1.set_title("Ratings Disable", fontsize=16)
plt.subplot(2,2,3)
g2= sns.countplot(x='video_error_or_removed', data=df)
g2.set_title("Video Error or Removed", fontsize=16)
print(plt.show())