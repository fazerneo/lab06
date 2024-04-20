lyrics = ''' Road shimmer wigglin' the vision
Heat, heat waves, I'm swimmin' in a mirror
Road shimmer wigglin' the vision
Heat, heat waves, I'm swimmin' in a
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
Usually I put somethin' on TV
So we never think about you and me
But today I see our reflections
Clearly in Hollywood, layin' on the screen
You just need a better life than this
You need somethin' I can never give
Fake water all across the road
It's gone now, the night has come, but
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
You can't fight it, you can't breathe
You say something so lovin', but
Now I gotta let you go
You'll be better off in someone new
I don't wanna be alone
You know it hurts me too
You look so broken when you cry
One more and then I say goodbye
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
I just wonder what you're dreamin' of
When you sleep and smile so comfortable
I just wish that I could give you that
That look that's perfectly un-sad
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Heat waves been fakin' me out
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
Sometimes, all I think about is you
Late nights in the middle of June
Heat waves been fakin' me out
Can't make you happier now
Road shimmer wigglin' the vision
Heat, heat waves, I'm swimmin' in a mirror
Road shimmer wigglin' the vision
Heat, heat waves, I'm swimmin' in a mirror '''
        
list = lyrics.split()

def frequency(song_lyrics):
    
    dict = {}

    for word in song_lyrics:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    return dict

dict = frequency(list)


def highAndlow(frequency_dict):

    high = []
    low = []
    tempHigh = []
    tempLow = []
    highFreq = max(frequency_dict.values())
    lowFreq = min(frequency_dict.values())

    for key, value in frequency_dict.items():
        
        if value == highFreq:
            if key not in tempHigh:
                tempHigh.append(key)

        if value == lowFreq:
            if key not in tempLow:
                tempLow.append(key)
    
    return [tempHigh, highFreq], [tempLow, lowFreq]

(high, low) = highAndlow(dict)

print(f"words with highest frequency \n{high}")
print()
print(f"words with lowest frequency \n{low}")
print()