import requests
from bs4 import BeautifulSoup

class YoutubeSearch():

    def __init__(self):
        self.base_url = "https://vid.puffyan.us/search?q={}&page={}&type={}"

    def search(self, args: str, page: int = 1, type: str = 'video') -> dict:
        r"""Searches for a list of videos.

    args: Keywords to search..
    page: (optional) Integer for the result page..
    type: (optional) "video", "channel" or "playlist". Gives only the selected type.
    return: dict
    """
        # format base url as per user args
        type = type.lower() # Just in case user gives capitalization.
        url = self.base_url.format(args.replace(' ', '+'), page, type)
        # check if args are not None.
        if args == '':
            raise ValueError('No search arguments were given!')
        # request the page
        resp = requests.get(url)
        # if the response is not ok, then raise the error
        if resp.status_code != 200:
            resp.raise_for_status()
        # if success, parse the content in soup
        soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
        if type == 'channel':
            # if channel then get channel names instead of titles. also replace the verified tick.
            names = [name.get_text().replace('\xa0', '') for name in soup.select('a p')]
            subs = [subs.get_text() for subs in soup.select('a+ p')]
            profilepics = ['https://vid.puffyan.us' + pfp['src'] for pfp in soup.select('img')]
            videos = [video.get_text() for video in soup.select('p+ p')]
            links = [link.a['href'] for link in soup.select('.pure-u-md-1-4 .h-box')]
            output = [{'name': names[i], 'subscribers': subs[i], 'links': links[i],'profile': profilepics[i]} for i in range(len(names))]
            result = {'success': True, 'results': output}
        elif type == 'video':  
            # if video then get video information
            channels = [channel.get_text().replace('\xa0', '') for channel in soup.select('.channel-name')]
            videos = [video.get_text() for video in soup.select('div+ p')]
            links = [link.a['href'] for link in soup.select('.pure-u-md-1-4 .h-box')]
            output = [{'channel': channels[i], 'title': videos[i], 'link': links[i]} for i in range(len(channels))]
            result = {'success': True, 'results': output}
        elif type == 'playlist':
            # if playlist then get playlist information
            names = [name.get_text().replace('\xa0', '') for name in soup.select('div+ p')]
            channelnames = [channel.get_text().replace('\xa0', '') for channel in soup.select('b')]
            links = [link.a['href'] for link in soup.select('.pure-u-md-1-4 .h-box')]
            output = [{'title': names[i], 'channel': channelnames[i], 'link': links[i]} for i in range(len(names))]
            result = {'success': True, 'results': output}
        else:
            # if anything else, raise error
            raise ValueError('Only "video", "channel" and "playlist" is accepted as type!')
        return result
    
    def info(self, link: str) -> dict:
        r"""Get information of a video using link.

    link: Video URL of the video you want information of. .
    return: dict
    """
        if 'youtu.be' in link:
            videoid = link.split('be/')[-1]
        else:
            videoid = link.split('watch?v=')[-1]
        link = f'https://vid.puffyan.us/watch?v={videoid}'
        resp = requests.get(link).content
        soup = BeautifulSoup(resp, 'html.parser', from_encoding='utf-8')
        title = ' '.join(soup.select('h1')[0].get_text().split())
        views = soup.select('#views')[0].get_text().replace(' ', '')
        channel = soup.select('#channel-name')[0].get_text().replace('\xa0', '')
        thumb = f"https://vid.puffyan.us/vi/{videoid}/maxres.jpg"
        return {'success': True, 'title': title, 'views': views, 'channel': channel, 'thumbnail': thumb} 

