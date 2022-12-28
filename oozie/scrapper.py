# import praw
# import pandas as pd
#
# reddit = praw.Reddit(client_id='oipIm2GxfZBd77OBwOPyvA', client_secret='DYC59MfqbuAhpwIpgZGx_IBDnk99zA', user_agent='BDEproj')
#
# hot_posts = reddit.subreddit('MachineLearning+AskHistorians+philosophy').top(time_filter= "week", limit=1000)
# posts = []
#
# for post in hot_posts:
#     sub = post.subreddit.display_name
#     title = post.title
#     title = title.replace(",", "")
#     desc = post.selftext
#     desc = desc.replace(",", "")
#     text = title + ' ' + desc
#     link = post.permalink
#     id = post.id
#     posts.append([sub, title, text, link, id])
#
# posts = pd.DataFrame(posts,columns=['subreddit', 'title', 'text', 'link', 'id'])
# posts.to_csv('posts.csv', index = False)


print("HELLO")
with open('HELL.txt', 'x') as f:
    f.write('Create a new text file!')

#with open('hdfs://au/user/pk.stradomski-ece/oozie/HELLOO.txt', 'x') as f:
#    f.write('Create a new text file!')
