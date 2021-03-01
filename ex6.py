import tweepy

ACCESS_TOKEN = '776512451756036097-aqEVHHXBHykKczmCbzwmBFzZXodHpzj'
ACCESS_TOKEN_SECRET = 'YtOJjgcxIcUxpAoCUQWNs6HoLga64MLmaEAMvdghI1mso'
CONSUMER_KEY = 'Ogu1N7bTxod6M3aHN6g6tSehl'
CONSUMER_KEY_SECRET = 'Ha2krPXYAllPLlXyBk5FrSq16crlx8IYmSp3SBbMo7gClCL7Ir'

def ConnectToTwitter():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api

api = ConnectToTwitter()


user = input("user:")#παίρνω τις λέξεις απο τα 10 τελευταια tweets απο τον λογαριασμό που μου δίνει ο χρήστης
word_list=[]
userstweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in userstweets:
    word_list.append(tweet.text)

oiLekseis=[]
for tweet in word_list:
    spasmenes = tweet.split()#τις χωρίζω σε λέξεις
    oiLekseis = oiLekseis + spasmenes

def Sorting(oiLekseis):
    oiLekseis.sort(key=len)#και τις ταξινομώ με αύξουσα σείρα μεγέθους
    return oiLekseis

print(Sorting(oiLekseis))

SYMBOLA = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

Apotelesmata = []
for leksh in oiLekseis:#βρίσκω και αφαιρώ τα σύμβολα απο τις λέξεις
    proswrino = ""
    for gramma in leksh:
        if gramma not in SYMBOLA:
            proswrino += gramma

    Apotelesmata.append(proswrino)


for i in range(5):#βρίσκω τις 5 μικρότερες και τις 5 μεγαλύτερες λέξεις και τις εμφανίζω όπως ζητάει η άσκηση   
    print(Apotelesmata[i])

for j in reversed(range(len(Apotelesmata)-5,len(Apotelesmata))):
    print(Apotelesmata[j])
