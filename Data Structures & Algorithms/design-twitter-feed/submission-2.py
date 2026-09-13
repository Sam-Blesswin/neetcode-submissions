class Twitter:

    def __init__(self):
        self.posts = {}
        self.follows = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.timestamp += 1
        self.posts[userId].append([self.timestamp,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        maxheap = []
        followers = set()

        if userId in self.follows:
            followers = self.follows[userId]
        followers.add(userId)

        for followerId in followers:
            if followerId not in self.posts:
                continue

            n = len(self.posts[followerId])
            tweet = self.posts[followerId][n-1]
            heapq.heappush(maxheap,[-tweet[0],tweet[1],followerId, n-1])
        
        while maxheap and len(feed)<10:
            res = heapq.heappop(maxheap)
            tweetId = res[1]
            fid = res[2]
            idx = res[3]

            feed.append(tweetId)

            if idx>0:
                tweet = self.posts[fid][idx-1]
                heapq.heappush(maxheap,[-tweet[0],tweet[1],fid, idx-1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
        
