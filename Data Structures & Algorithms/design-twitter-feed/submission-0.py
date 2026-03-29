class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_users = {userId}
        if userId in self.follows:
            feed_users.update(self.follows[userId])
        
        res = []
        for uId in feed_users:
            if uId in self.tweets:
                res.extend(self.tweets[uId])
        
        res.sort(key=lambda x: x[0], reverse=True)
        return [t[1] for t in res[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId != followerId:
            self.follows[followerId].discard(followeeId)