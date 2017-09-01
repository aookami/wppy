import twitter
import sys
from collections import Counter

#set badword dictionary

badwords = 'I your like just dont some can this they you im what out when up should how if live youre 2me will who ? ?? ??? the he she it be in of and to is on for i be at we as it by so has my a i RT and is of in this you for my u are it all on but that by so r if be we w ur its not i at  '
badwords = badwords + 'do these any said really even over same then now The Just a lot would make sure their thing there'

badwordlist = badwords.split()

#set twitter api credentials
api = twitter.Api(consumer_key='DJQsTwp76jumAZFpRuB4CZtZd',consumer_secret='hpDA6nOrxxseymmDioOOW9ypKxYUAN4P4AyX8hIvqfZhf6iNCv',  access_token_key='903723060909498368-EAeJ3IxExdAb9YSSBguhnAp9ksHh9qC', access_token_secret='Pwi77bW61lloVsvOpiPBHgAJt0YDuzzp8HfINXilG7bwQ')

screenname = sys.argv[1]

print(api.VerifyCredentials())
#authenticates the application

tweets = api.GetUserTimeline(screen_name=screenname, count=200)
#pulls the last 200 tweets from the# 
#user id specified in the first field#
textfile = ' '

for item in tweets:
	textfile = textfile + ' ' + item.text

wordcount = Counter(textfile.split())

for item in list(wordcount):
	if item in badwordlist:
		del wordcount[item]


for item in wordcount.most_common(50):
	print(item)
#for item in wordcount.most_common(50):
#	item = item.lower()
