#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python 
import praw
import os
import time

BOT_NAME = "replieswinkytoOwnfir"
friend = 'Ownfir'
username = 'replieswinkytoOwnfir'
password = 'redditbot1234'
message = ';)'

user_agent = ("Winky face to my friend Ownfir version 0.1 by /u/keepitsalty")
r = praw.Reddit(user_agent = user_agent)

print (time.strftime("%m/%d/%Y"))
print (time.strftime("%H:%M:%S"))
print 'Logging in'
r.login(username, password, disable_warning=True)
print 'Login successful'

print 'Acquiring User & Comments'
user = r.get_redditor(friend)


comment_limit = 1
gen = user.get_comments(limit=comment_limit)


def record_comment(id):
    comments_replied_to.append(comment.id)
    with open("comments_replied_to.txt", "w") as f:
        f.write(id + "\n")  

if not os.path.isfile("comments_replied_to.txt"):
    print 'Acquiring comments'
    user = r.get_redditor(friend)
    comments = user.get_comments()
    print 'Creating comments_replied_to.txt'
    with open("comments_replied_to.txt", "w") as f:
        for comment in comments:
            id = comment.id
            f.write(id + "\n")   
    print 'comments_replied_to.txt created'

with open("comments_replied_to.txt", "r") as f:
    print 'Reading comments_replied_to.txt'
    comments_replied_to = f.read()
    comments_replied_to = comments_replied_to.split("\n")
    comments_replied_to = filter(None, comments_replied_to)
    print 'comments_replied_to.txt read'

print comments_replied_to

for comment in gen:
   if comment.id not in comments_replied_to:
      print 'Replying to ' + str(comment)
      comment.reply(message)
      record_comment(comment.id)
      print comments_replied_to

   elif comment.id in comments_replied_to:
      print('bot already replied')
print "\n" 
exit()
