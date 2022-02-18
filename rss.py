#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install feedparser


# In[3]:


import feedparser
# url of blog feed
feed_url = "https://vaibhavkumar.hashnode.dev/rss.xml"
  
blog_feed = feedparser.parse(feed_url)


# In[4]:


# returns title of the blog site
blog_feed.feed.title 
  
# returns the link of the blog
# and number of entries(blogs) in the site.
blog_feed.feed.link
len(blog_feed.entries)
  
# Details of individual blog can
# be accessed by using attribute name
print(blog_feed.entries[0].title)
print(blog_feed.entries[0].link)
print(blog_feed.entries[0].author)
print(blog_feed.entries[0].published)


# In[7]:


def get_posts_details(rss=None):
    
    """
    Take link of rss feed as argument
    """
    if rss is not None:
        
          # import the library only when url for feed is passed
        import feedparser
          
        # parsing blog feed
        blog_feed = blog_feed = feedparser.parse(rss)
          
        # getting lists of blog entries via .entries
        posts = blog_feed.entries
          
        # dictionary for holding posts details
        posts_details = {"Blog title" : blog_feed.feed.title,
                        "Blog link" : blog_feed.feed.link}
          
        post_list = []
          
        # iterating over individual posts
        for post in posts:
            temp = dict()
              
            # if any post doesn't have information then throw error.
            try:
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass
              
            post_list.append(temp)
          
        # storing lists of posts in the dictionary
        posts_details["posts"] = post_list 
          
        return posts_details # returning the details which is dictionary
    else:
        return None
  
if __name__ == "__main__":
  import json
  
  feed_url = "https://vaibhavkumar.hashnode.dev/rss.xml"
  
  data = get_posts_details(rss = feed_url) # return blogs data as a dictionary
    
  if data:
    # printing as a json string with indentation level = 2
    print(json.dumps(data, indent=2)) 
  else:
    print("None")


# In[ ]:




