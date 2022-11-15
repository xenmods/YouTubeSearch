from YouTubeSearch.youtube import YoutubeSearch
import json

# Search using keywords and on page 2
search = YoutubeSearch()
result = search.search('advanced python tutorial', type='playlist')
if result['success']:
    print(json.dumps(result, indent=4))

# Get information of a video
result = search.info('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
if result['success']:
    print(json.dumps(result, indent=4))
