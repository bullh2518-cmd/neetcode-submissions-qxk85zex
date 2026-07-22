import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = [userId] + list(self.following.get(userId, set()))

        for followee in users:
            if followee in self.tweets:
                for time, tweetId in self.tweets[followee]:
                    heapq.heappush(heap, (time, tweetId))

        feed = []

        while heap and len(feed) < 10:
            time, tweetId = heapq.heappop(heap)
            feed.append(tweetId)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)