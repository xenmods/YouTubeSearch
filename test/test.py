from YouTubeSearch import YoutubeSearch


# Search using keywords and on page 2
search = YoutubeSearch()
result = search.search('advanced python tutorial', page=2)
if result['success']:
    print(result)

# Get information of a video
result = search.info('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
if result['success']:
    print(result)
