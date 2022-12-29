import praw
import pandas as pd

reddit = praw.Reddit(client_id='oipIm2GxfZBd77OBwOPyvA', client_secret='DYC59MfqbuAhpwIpgZGx_IBDnk99zA', user_agent='BDEproj')

hot_posts = reddit.subreddit('MachineLearning+AskHistorians+philosophy').top(time_filter= "week", limit=1000)
posts = []

for post in hot_posts:
    sub = post.subreddit.display_name
    title = post.title
    title = title.replace(",", "")
    title = title.replace("\n", "")
    desc = post.selftext
    desc = desc.replace(",", "")
    desc = desc.replace("\n", "")
    content = title + ' ' + desc
    link = post.permalink
    id = post.id
    posts.append([sub, title, content, link, id])

posts = pd.DataFrame(posts,columns=['subreddit', 'title', 'content', 'link', 'id'])
posts.to_csv('posts.csv', index = False, line_terminator='\n')
