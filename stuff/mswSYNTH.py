import praw
import os
from time import sleep
from gtts import gTTS

# You need to install gTTS and mpg321 on your machine

PORT = int(os.environ.get('PORT', 5000))

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')


def __speak__(comment):
    if comment.author != 'AutoModerator':
        text = comment.body
        language = 'de'  # todo automatically detect language
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("msw-comment.mp3")
        os.system("mpg321 msw-comment.mp3")
        os.remove("msw-comment.mp3")
        sleep(1)


# all comments
def __readcomment__(comment_queue):
    # todo save first comment to not play it again
    while comment_queue:
        print('queue: ' + str(len(comment_queue)))
        comment = comment_queue.pop(0)
        __speak__(comment)
        if (len(comment.replies) > 0):
            print('comments: ' + str(len(comment.replies)))
            __readreplies__(comment.replies)
            print('comments up')


# through replies recursive
def __readreplies__(replies):
    for reply in replies:
        __speak__(reply)
        if (len(reply.replies) > 0):
            __readreplies__(reply.replies)


def main():
    sub = reddit.subreddit("mauerstrassenwetten")
    while True:
        for submissions in sub.hot(limit=4):
            if submissions.stickied:
                if ('Tägliche Diskussion ' in submissions.title) or ('Pläne ' in submissions.title):
                    submissions.comment_sort = 'new'
                    submissions.comments.replace_more(limit=20)
                    comment_queue = submissions.comments[:]
                    __readcomment__(comment_queue)


if __name__ == "__main__":
    main()
