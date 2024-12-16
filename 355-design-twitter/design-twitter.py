class Twitter:

    def __init__(self):
        self.tweets = []
        self.Follow = defaultdict(set) 
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId,tweetId,self.timestamp]
        self.tweets.append(tweet)
        self.timestamp+=1
        
        

    from typing import List
from collections import defaultdict
from heapq import nlargest

class Twitter:

    def __init__(self):
        self.tweets = []  # List to store tweets: [userId, tweetId, timestamp]
        self.Follow = defaultdict(set)  # Key=followerId, Value=set of followeeIds
        self.timestamp = 0  # Incremental timestamp for ordering tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId, tweetId, self.timestamp]
        self.tweets.append(tweet)  # Add tweet to the list
        self.timestamp += 1  # Increment timestamp for uniqueness

    def getNewsFeed(self, userId: int) -> List[int]:
        
        followees = self.Follow[userId] | {userId}  

       
        relevant_tweets = [tweet for tweet in self.tweets if tweet[0] in followees]

      
        most_recent_tweets = nlargest(10, relevant_tweets, key=lambda x: x[2])

       
        return [tweet[1] for tweet in most_recent_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:  
            self.Follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
       
        if followeeId in self.Follow[followerId]:
            self.Follow[followerId].remove(followeeId)

        

 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)