import lyricsgenius
import random
import tweepy


#Input API Keys and tokens as found on GENIUS
keys = {
	'CONSUMER_API_KEY': 'M8QkUPVcrBj45LcAoPCtnAun0',
	'CONSUMER_API_SECRET_KEY': 'oG3DPDZ7RLshcXWars7rFoSEptbfzl3YcfoQiyvot4EbGlXYE7',
	'ACCESS_TOKEN': '1555242902858735618-Z1Hp8oIAER9c2VG2TtUeK13wkmE8l9',
	'ACCESS_TOKEN_SECRET': '7eNTjNBBeqjwYxi35VTRn6s4p58hKaTLPmfVQ0SxzxgbV'
	}
genius = lyricsgenius.Genius ("1q4nreQz569w-aRJKDJOrUrepX3gduBPPTnoOLtHhSkepmsLMx-rfZv_8V7Nl2YW")
artist = genius.search_artist("Babyface Ray")
print(artist.songs)

#Once you run your code another window will open with a song list, copy and paste the songs you wish

all_songs =  ["My Thoughts Part II","Paperwork Party", "Gallery Dept", "#1 Fan", "Hall of Fame", "If You Know You Know", "Start This Over", "Like Daisy Lane","Real Niggas Don’t Rap","Fake Luv","Real","Ashanti","What The Business Is","A Million Cash Race","Fuck Summer Jamz","Legend","Sincerely Face","Family﹥Money","Miami In November","I Went To New York","Touchdown","Tap In","Scared of Them","My Thoughts  / Pop’s Prayer","Addy","Tahoe","Rip Jas","Change My #","I Got Use to This","Pink 10s","Steve Francis","Let Me Down","6 Mile Show","Still Gone Bust a Band","Overtime","Foreva","Free Spazzo","Blood Sweat & Tears","Mob","Tunnel Vision","Football Pads","In the Game","Motown Music","Allowance","Me, Wife & Kids","Ron Artest","Move to LA","Give No Fucks","Better Days","Change You","Steak N Lobster","Didn’t Panic","Spending Spree","Palm Angels, Palms Itching","Kingpin","Off Rap","You Can’t Get a Verse","Seduction","No Limit Soldiers","Idols","Back N Action","Richard Flair", "Same Pain", "Needed Some Love", "They Think I Rap My Brother’s Life","Catch It","My Thoughts", "Kush & Codeine", "Trill Spill", "Time 11AM / 8PM", "Go Yard", "Flowers When I’m Alive", "Too Many", "Big Estate", "Lynch Em", "Fell in Love", "Illmatic", "RIP, Pt.1 "
 "oz", "Snow Globe","XXL Freshman Freestyle Babyface Ray"]
 
 #This command pulls the lyrics from a random song you pasted

def get_raw_lyrics():
	genius_client_access_token = "1q4nreQz569w-aRJKDJOrUrepX3gduBPPTnoOLtHhSkepmsLMx-rfZv_8V7Nl2YW"
	genius = lyricsgenius.Genius(genius_client_access_token)
	random_song_title = random.choice(all_songs)
	lyrics = genius.search_song(random_song_title, "Babyface Ray").lyrics
	song = random_song_title.upper()
	return lyrics, song

#These commands split the lyrics into 2 lines and scrubs lines of blank text, then tweets it

def get_tweet_from(lyrics):
	lines = lyrics.split('\n')
	for index in range (len(lines)):
		if lines[index] == "" or "[" in lines [index]:
			lines[index] = "XXX"
		lines = [i for i in lines if i != "XXX"]
		
		random_num = random.randrange(0, len(lines)-1)
		tweet = lines[random_num] + "\n" + lines[random_num+1]
		tweet = tweet.replace("\\","")
		return tweet
	
	#This handler is required to allow AWS Lambda to read and execute your script
		
def handler(event, context):
	auth = tweepy.OAuthHandler(
		keys['CONSUMER_API_KEY'],
		keys['CONSUMER_API_SECRET_KEY']
	)
	auth.set_access_token(
		keys['ACCESS_TOKEN'],
		keys['ACCESS_TOKEN_SECRET']
    )
	api = tweepy.API(auth)
	lyrics, song = get_raw_lyrics()
	tweet = get_tweet_from(lyrics)
	status = api.update_status(tweet)
	bio = api.update_profile(description=song)
	
	return tweet