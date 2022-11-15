# [YouTubeSearch](https://github.com/xenmods/YouTubeSearch)

##### Search for YouTube videos, channels & playlists. Get video information using link. WITHOUT YouTube Data API v3.



## Installing

```bash
pip install 
```

## Usage<br /><br />

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

</details><br />

#### Search for only channels

```python
from YouTubeSearch import YouTubeSearch
search = YouTubeSearch()
videossearch = search.search('advanced python tutorial', type='channel')
print(videossearch)
```

<details><br />
 <summary> Example Result</summary>

```json
{
    "success": true,
    "results": [
        {
            "name": "Alex The Analyst",
            "subscribers": "315,000 subscribers",
            "links": "/channel/UC7cs8q-gJRlGwj4A8OmCmXg",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu9iyZu10NYIbwWmmYU2MJw5uifKxocE9AjDed9W=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "thenewboston",
            "subscribers": "2,650,000 subscribers",
            "links": "/channel/UCJbPGzawDH1njbqV-D5HqKw",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu8OByGsgirSfHbmWD8P6vXknx2fR-QjlutAFwvRKg=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Python Esper",
            "subscribers": "3,370 subscribers",
            "links": "/channel/UCZKyNYzMqHOMxIkOBItWL7Q",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu_DRGKqu9JBJs9WiCEN22x_aAGuRJ9OpgTx3kwx=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "CodeWithRonny",
            "subscribers": "514 subscribers",
            "links": "/channel/UCLartwibE5_76F8uuB2Zo3w",
            "profile": "https://vid.puffyan.us/ggpht/EvpccvUDD0CS6PTFcWuj8PBzz9FnUvX5lFM7k1L7M3smrXc0bvZ91ktcREEnQIKKbHuubiA2WwI=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Python Engineer",
            "subscribers": "204,000 subscribers",
            "links": "/channel/UCbXgNpp0jedKWcQiULLbDTA",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu-WpknCmw6HBcttsSBGlN7nugz-yUQ3mZTm3dWPqA=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "freeCodeCamp.org",
            "subscribers": "6,710,000 subscribers",
            "links": "/channel/UC8butISFwT-Wl7EV0hUK0BQ",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu9UWrGceKWaqm8AF89vuxrEt8MO3E59qOoQ785Lew=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Eternal Guru",
            "subscribers": "1,080 subscribers",
            "links": "/channel/UCaNJxOXoFYhkEJ5hu69lx7g",
            "profile": "https://vid.puffyan.us/ggpht/jpt8MuNZRBGL6NLVjL4Z6Rx3DY7Km-NHsRO2FsBEcV2YfxZ5abO3tzc0ztIjcFK9IJJRmItIRQ=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Telusko",
            "subscribers": "1,850,000 subscribers",
            "links": "/channel/UC59K-uG2A5ogwIrHw4bmlEg",
            "profile": "https://vid.puffyan.us/ggpht/o4MZVi2qdNgx0K7vpEl7DT2PefjROdisZTD7is6TMimF1_DTM49O1ld3iQzTpE5MCj86c-vzav8=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "PyMate",
            "subscribers": "125 subscribers",
            "links": "/channel/UCI79Wkb_O-Rn0Gy-Jq3V-ag",
            "profile": "https://vid.puffyan.us/ggpht/enuPhC7NVTONmbRQTsiQmIztSvSUobz-iBkCI6mgs8xL95mFyPFaNywD5eZN0iuyphwZ6Jx1=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Dave Gray",
            "subscribers": "92,300 subscribers",
            "links": "/channel/UCY38RvRIxYODO4penyxUwTg",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu-hi-TxVHQwPnZh3h9-F0OAQyqoETBJQWXjDzILGg=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Just coding",
            "subscribers": "4 subscribers",
            "links": "/channel/UCPtEEU4xJO22s2Q7LzcZM1Q",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu9Uxd7sSSaVWowFPx2-LnR_xL8UtFHKuOooF3J0_YhaD2iyEZxVIan1467cASrz=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Programming with Mosh",
            "subscribers": "2,910,000 subscribers",
            "links": "/channel/UCWv7vMbMWH4-V0ZXdmDpPBA",
            "profile": "https://vid.puffyan.us/ggpht/tBEPr-zTNXEeae7VZKSZYfiy6azzs9OHowq5ZvogJeHoVtKtEw2PXSwzMBKVR7W0MI7gyND8=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "oTree tutorials",
            "subscribers": "401 subscribers",
            "links": "/channel/UCI-kL2lFnRZ73GbmhJfWo4w",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu_H_RshZGq2QdWYwz1uuowcQVox-ywPNGOXLQ=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Amit Thinks",
            "subscribers": "79,500 subscribers",
            "links": "/channel/UCgnr2Lkl1LZf0IOKRDAoJ2g",
            "profile": "https://vid.puffyan.us/ggpht/QTFCc3CQhVsSgsuNw6nsfMhSCHyYRkv064U1iyseYt2XRSYZLpSjQWJuIhhzXJeK2vgIOtNBEw=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Python Programming",
            "subscribers": "6,960 subscribers",
            "links": "/channel/UC4sG9NWzpLX3rvYE9g3aAQw",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu976HGyWOXP-A0Cr1MbWnvtescs6Y_ixUraxHryBA=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Geo-Python",
            "subscribers": "2,510 subscribers",
            "links": "/channel/UCQ1_1hZ0A1Vic2zmWE56s2A",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu_xjjfw4L567Ga-ZwalXmBS2gWjzBxvwsWicjQE=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Learn Computer vlog",
            "subscribers": "1 subscriber",
            "links": "/channel/UClLY1twA_yMmvcjRjbPXTOw",
            "profile": "https://vid.puffyan.us/ggpht/fNXku5lYK107L70iYo3_iVxWb2icfc70x4__4pi7mZc1ttIGEb5dcsEgYXIHRfHoFobMSbMh_w=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "programming-with-mohammed",
            "subscribers": "517 subscribers",
            "links": "/channel/UCMWDPNicIA74HBc_y8DrxiQ",
            "profile": "https://vid.puffyan.us/ggpht/pXmKCRVUBp-C8Ie5dweiEMxTlyLH1xvXW39EVNhWw19O1zQ1onf8dZlGq8G-qbKcXEEerU2k9Q=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "cs3157: Advanced Programming",
            "subscribers": "537 subscribers",
            "links": "/channel/UCV9z9mH8hHet6mTVy0gNWfg",
            "profile": "https://vid.puffyan.us/ggpht/ytc/AMLnZu9ehbIQ2x2i28o63gL-kqjhEDQAQXFPoPqa_nme=s176-c-k-c0x00ffffff-no-rj-mo"
        },
        {
            "name": "Sreekanth",
            "subscribers": "2,480 subscribers",
            "links": "/channel/UCjRVKSokBHlljocLdnUD9pg",
            "profile": "https://vid.puffyan.us/ggpht/VtewN2lJt1kq-mZl79TnY1r9m03ns2vCj0W-us9Ia-pzKhB9ULae2hNKpQ3BMH72QJlk_V0O=s176-c-k-c0x00ffffff-no-rj-mo"
        }
    ]
}
```

</details><br />


#### Search for only playlists

```python
from YouTubeSearch import YouTubeSearch
search = YouTubeSearch()
videossearch = search.search('advanced python tutorial', type='playlist')
print(videossearch)
```


<details>
 <summary> Example Result</summary>

```json
{
    "success": true,
    "results": [
        {
            "title": "Python Advanced Tutorials",
            "channel": "NeuralNine",
            "link": "/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc"
        },
        {
            "title": "Advanced Python - Complete Course",
            "channel": "Python Engineer",
            "link": "/playlist?list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2"
        },
        {
            "title": "Advanced Python Tutorial by DURGA Sir",
            "channel": "Durga Software Solutions",
            "link": "/playlist?list=PLd3UqWTnYXOkzPunQOObl4m_7i6aOIoQD"
        },
        {
            "title": "Advanced Python Programming Tutorials",
            "channel": "TheCodex",
            "link": "/playlist?list=PLB5jA40tNf3uCLarFvR0dS0kDwC-VU0Z9"
        },
        {
            "title": "Advance Python (Hindi)",
            "channel": "Geeky Shows",
            "link": "/playlist?list=PLbGui_ZYuhijd1hUF2VWiKt8FHNBa7kGb"
        },
        {
            "title": "Python3 Advanced Tutorials",
            "channel": "DrapsTV",
            "link": "/playlist?list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d"
        },
        {
            "title": "Advanced Python Programming in Tamil",
            "channel": "CS in Tamil",
            "link": "/playlist?list=PLWbtDrDnmTHDkyMizWD577tHixGE0I2c4"
        },
        {
            "title": "Advanced Python",
            "channel": "MrSensharma",
            "link": "/playlist?list=PLTOBJKrkhpoMdsT9RUERSDdEVrViykAEQ"
        },
        {
            "title": "Expert Python Tutorials",
            "channel": "Tech With Tim",
            "link": "/playlist?list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP"
        },
        {
            "title": "Python Mastery Course | Python Tutorial for Beginner to Advanced - 2022 \ud83d\udd25",
            "channel": "WsCube Tech",
            "link": "/playlist?list=PLjVLYmrlmjGfoEhXh-ef5QwVCvtWANoTR"
        },
        {
            "title": "The Complete Python Masterclass Learn Python From Scratch (Beginner To Advanced)",
            "channel": "CodeDonor",
            "link": "/playlist?list=PLIrsP8dft12CSv-KEbiXq21JmR3LUr854"
        },
        {
            "title": "Complete Python Tutorial for Beginners to Advanced in Hindi - 2022 \ud83d\udd25",
            "channel": "WsCube Tech",
            "link": "/playlist?list=PLjVLYmrlmjGcQfNj_SLlLV4Ytf39f8BF7"
        },
        {
            "title": "Python Core And Advance Tutorial",
            "channel": "DS Computer Science World",
            "link": "/playlist?list=PLPeqhD4jhR8gFSJVn2X188A7vap88GBie"
        },
        {
            "title": "Advanced Python Tutorials",
            "channel": "PyLenin",
            "link": "/playlist?list=PLqEbL1vopgvsv6jz8xB3Aa6w1njhf3egY"
        },
        {
            "title": "Intermediate/Advanced python Tutorials in Hindi",
            "channel": "CodeWithHarry",
            "link": "/playlist?list=PLu0W_9lII9aiJWQ7VhY712fuimEpQZYp4"
        },
        {
            "title": "Intermediate Python Tutorials",
            "channel": "Tech With Tim",
            "link": "/playlist?list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv"
        },
        {
            "title": "Advanced Python by Durga sir",
            "channel": "Durga Software Solutions",
            "link": "/playlist?list=PLd3UqWTnYXOmGUvVAToLPZOnj8HqMlFp5"
        },
        {
            "title": "Python Tutorials",
            "channel": "Corey Schafer",
            "link": "/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
        },
        {
            "title": "Advanced Python Scripting | Arpit Jain",
            "channel": "CodeBeyond",
            "link": "/playlist?list=PLN4aKSfpk8TRM-WnQplsCUxXAHJik3WaZ"
        },
        {
            "title": "Python Tutorials For Absolute Beginners In Hindi",
            "channel": "CodeWithHarry",
            "link": "/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME"
        }
    ]
}
```

</details><br /><br />



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

</details><br />

## Information

- All the research, for making this library possible, is entirely done by myself.
- This is just a fun project for me. I use it myself.
- Uses Web Scraping (bs4) 
- I will update it soon with more features
