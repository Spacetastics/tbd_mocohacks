from googleapiclient.discovery import build
import config

urlcopy = "https://www.youtube.com/watch?v="
yt = build('youtube', 'v3', developerKey=key)
videoid = []

topic = ""
num = 0
leng = ""
class Search:
    def __init__(self, tx, nm, ln):
        self.topic = tx
        self.num = nm
        self.leng = ln
        super().__init__(tx, nm, ln)
    pass



n = Search(topic, num, leng)
numR = int(num)

k = yt.search().list(
    part='snippet',
    q=topic,
    topicId="/m/01k8wb",
    type = 'video',
    videoDuration = leng,
    order='relevance',
    relevanceLanguage="en",
    maxResults=numR
).execute()
print(k)

for result in k.get("items", []):
    videoid.append("%s" % (result["id"]["videoId"]))

print ("\n".join(videoid))

for i in range(numR):
    print (urlcopy + videoid[i])
