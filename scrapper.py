import praw
import pandas as pd

reddit = praw.Reddit(client_id='oipIm2GxfZBd77OBwOPyvA', client_secret='DYC59MfqbuAhpwIpgZGx_IBDnk99zA', user_agent='BDEproj')

hot_posts = reddit.subreddit('MachineLearning').top(time_filter= "week", limit=100)
posts = []

for post in hot_posts:
    title = post.title
    title = title.replace(",", "")
    desc = post.selftext
    desc = desc.replace(",", "")
    text = title + ' ' + desc
    link = post.permalink
    id = post.id
    posts.append([title, text, link, id])

posts = pd.DataFrame(posts,columns=['title', 'text', 'link', 'id'])
posts.to_csv('posts.csv', index = False)
