# [YouTubeSearch](https://github.com/xenmods/YouTubeSearch)

##### Search for YouTube videos, channels & playlists. Get video information using link. WITHOUT YouTube Data API v3.



## Installing

```bash
pip install 
```

## Usage

#### Search for only videos

```python
from YouTubeSearch import YouTubeSearch
search = YouTubeSearch()
videossearch = search.search('advanced python tutorial', type='video')
print(videossearch)
```

<details>
 <summary> Example Result</summary>

```json
{
    "success": true,
    "results": [
        {
            "channel": "Simplilearn",
            "title": "Object Oriented Programming In Python | Python Object Oriented Programming Advanced | Simplilearn",
            "link": "/watch?v=waUVA9K2CYg"
        },
        {
            "channel": "Master Programing",
            "title": "Python Advance Tutorial In Hindi",
            "link": "/watch?v=q3g2Yb-gMA0"
        },
        {
            "channel": "Python Engineer",
            "title": "Lists in Python - Advanced Python 01 - Programming Tutorial",
            "link": "/watch?v=QLTdOEn79Rc"
        },
        {
            "channel": "Python Engineer",
            "title": "Lambda in Python - Advanced Python 08 - Programming Tutorial - Map Filter Reduce",
            "link": "/watch?v=D2TJ9wvSP94"
        },
        {
            "channel": "Programming with Mosh",
            "title": "Python Functions | Python Tutorial for Absolute Beginners #1",
            "link": "/watch?v=u-OmVr_fT4s"
        },
        {
            "channel": "Socratica",
            "title": "List Comprehension  ||  Python Tutorial  ||  Learn Python Programming",
            "link": "/watch?v=AhSvKGTh28Q"
        },
        {
            "channel": "CS Dojo",
            "title": "How To Use Functions In Python (Python Tutorial #3)",
            "link": "/watch?v=NSbOtYzIQI0"
        },
        {
            "channel": "Telusko",
            "title": "#20 Python Tutorial for Beginners | While Loop in Python",
            "link": "/watch?v=HZARImviDxg"
        },
        {
            "channel": "Bro Code",
            "title": "Python Tutorial: Full Course for Beginners \ud83d\udc0d (FREE)",
            "link": "/watch?v=XKHEtdqhLK8"
        },
        {
            "channel": "Corey Schafer",
            "title": "Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters",
            "link": "/watch?v=jxmzY9soFXg"
        },
        {
            "channel": "freeCodeCamp.org",
            "title": "Advanced Computer Vision with Python - Full Course",
            "link": "/watch?v=01sAkU_NvOY"
        },
        {
            "channel": "Telusko",
            "title": "Python Tutorial for Beginners | Advance concepts",
            "link": "/watch?v=tQ1BJ3B8pSc"
        },
        {
            "channel": "Python Engineer",
            "title": "Logging in Python - Advanced Python 10 - Programming Tutorial",
            "link": "/watch?v=p0A4CV4MWd0"
        },
        {
            "channel": "freeCodeCamp.org",
            "title": "Learn Python - Full Course for Beginners [Tutorial]",
            "link": "/watch?v=rfscVS0vtbw"
        },
        {
            "channel": "Python Engineer",
            "title": "Strings in Python - Advanced Python 05 - Programming Tutorial",
            "link": "/watch?v=e6ivlABOYRI"
        },
        {
            "channel": "edureka!",
            "title": "Advanced Python Tutorial | Learn Advanced Python Concepts | Python Training | Edureka Rewind - 4",
            "link": "/watch?v=l-1WO0w9dk0"
        },
        {
            "channel": "Python Engineer",
            "title": "Itertools in Python - Advanced Python 07 - Programming Tutorial",
            "link": "/watch?v=3ecISAkioPc"
        },
        {
            "channel": "Python Engineer",
            "title": "JSON in Python - Advanced Python 11 - Programming Tutorial",
            "link": "/watch?v=EtAGd-3arNE"
        },
        {
            "channel": "TheCodex",
            "title": "Advanced Python Programming - GUI Automation with PyAutoGUI",
            "link": "/watch?v=1RE5tSPO2RI"
        },
        {
            "channel": "Python Engineer",
            "title": "Collections in Python - Advanced Python 06 - Programming Tutorial",
            "link": "/watch?v=UdcPhnNjSEw"
        }
    ]
}
```

</details>


### Get Video Information

```python
from YouTubeSearch import YouTubeSearch
search = YouTubeSearch()
videossearch = search.info('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(videossearch)
```

<details>
<summary> Example Result</summary>

```json
{
    "success": true,
    "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "views": "1,314,612,027",
    "channel": "Rick Astley",
    "thumbnail": "https://vid.puffyan.us/vi/dQw4w9WgXcQ/maxres.jpg"
}
```

</details>

## Information

- All the research, for making this library possible, is entirely done by myself.
- This is just a fun project for me. I use it myself.
- Uses Web Scraping (bs4) 
- I will update it soon with more features