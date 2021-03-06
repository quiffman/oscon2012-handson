#!/usr/bin/env python
import requests
import json
from requests.auth import HTTPBasicAuth
#
# Get Last 20 Tweets by Jack
#
# GET https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true
#          &include_rts=true&user_id=12
#
# user_id 12 has enabled geo, so we can see how places are shown in tweets
#
url='https://api.twitter.com/1/statuses/user_timeline.json'
payload={"user_id":"12"}
r = requests.get(url, params=payload)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
'''
Sample Output
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "2425",
  "content-type": "application/json;charset=utf-8",
  "date": "Sat, 23 Jun 2012 03:34:12 GMT",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sat, 23 Jun 2012 03:34:12 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "guest_id=\"v1:134042245239885200\";Expires=Mon, 23-Jun-14 03:34:12 GMT;Path=/;Domain=.twitter.com",
  "status": "200 OK",
  "x-frame-options": "SAMEORIGIN",
  "x-ratelimit-class": "api",
  "x-ratelimit-limit": "150",
  "x-ratelimit-remaining": "144",
  "x-ratelimit-reset": "1340424146",
  "x-transaction": "5cca2b8152532c86"
}
[
  {
    "contributors": null,
    "coordinates": {
      "coordinates": [
        11.791945,
        48.357173
      ],
      "type": "Point"
    },
    "created_at": "Thu Jun 21 13:42:22 +0000 2012",
    "favorited": false,
    "geo": {
      "coordinates": [
        48.357173,
        11.791945
      ],
      "type": "Point"
    },
    "id": 215801835590651904,
    "id_str": "215801835590651904",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": {
      "attributes": {},
      "bounding_box": {
        "coordinates": [
          [
            [
              11.764119,
              48.289745
            ],
            [
              11.893304,
              48.289745
            ],
            [
              11.893304,
              48.385797
            ],
            [
              11.764119,
              48.385797
            ]
          ]
        ],
        "type": "Polygon"
      },
      "country": "Germany",
      "country_code": "DE",
      "full_name": "Oberding, Erding",
      "id": "ad2f50942562790b",
      "name": "Oberding",
      "place_type": "city",
      "url": "http://api.twitter.com/1/geo/id/ad2f50942562790b.json"
    },
    "possibly_sensitive": false,
    "retweet_count": 44,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Camera on iOS</a>",
    "text": "Currently reading: http://t.co/svhUQw4P",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Thu Jun 21 12:31:43 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 215784060608450560,
    "id_str": "215784060608450560",
    "in_reply_to_screen_name": "StephenLepitak",
    "in_reply_to_status_id": 215764741308682240,
    "in_reply_to_status_id_str": "215764741308682240",
    "in_reply_to_user_id": 22925520,
    "in_reply_to_user_id_str": "22925520",
    "place": null,
    "retweet_count": 0,
    "retweeted": false,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "text": "@StephenLepitak thx!",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": {
      "coordinates": [
        7.020161,
        43.55106
      ],
      "type": "Point"
    },
    "created_at": "Wed Jun 20 19:31:29 +0000 2012",
    "favorited": false,
    "geo": {
      "coordinates": [
        43.55106,
        7.020161
      ],
      "type": "Point"
    },
    "id": 215527309225111552,
    "id_str": "215527309225111552",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": {
      "attributes": {},
      "bounding_box": {
        "coordinates": [
          [
            [
              6.944769,
              43.505012
            ],
            [
              7.074011,
              43.505012
            ],
            [
              7.074011,
              43.574785
            ],
            [
              6.944769,
              43.574785
            ]
          ]
        ],
        "type": "Polygon"
      },
      "country": "France",
      "country_code": "FR",
      "full_name": "Cannes, Alpes-Maritimes",
      "id": "57a1eb00d85de250",
      "name": "Cannes",
      "place_type": "city",
      "url": "http://api.twitter.com/1/geo/id/57a1eb00d85de250.json"
    },
    "possibly_sensitive": false,
    "retweet_count": 157,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Photos on iOS</a>",
    "text": "Accepting the #CannesLions Media Person of the Year award for our amazing users. Thank you! http://t.co/qIRyjdEb",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Wed Jun 20 15:53:39 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 215472490103836672,
    "id_str": "215472490103836672",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "retweet_count": 191,
    "retweeted": false,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "text": "Please join me in welcoming German football legend Franz @Beckenbauer to Twitter!",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": {
      "coordinates": [
        7.030183,
        43.547602
      ],
      "type": "Point"
    },
    "created_at": "Wed Jun 20 15:50:09 +0000 2012",
    "favorited": false,
    "geo": {
      "coordinates": [
        43.547602,
        7.030183
      ],
      "type": "Point"
    },
    "id": 215471605042782208,
    "id_str": "215471605042782208",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": {
      "attributes": {},
      "bounding_box": {
        "coordinates": [
          [
            [
              6.944769,
              43.505012
            ],
            [
              7.074011,
              43.505012
            ],
            [
              7.074011,
              43.574785
            ],
            [
              6.944769,
              43.574785
            ]
          ]
        ],
        "type": "Polygon"
      },
      "country": "France",
      "country_code": "FR",
      "full_name": "Cannes, Alpes-Maritimes",
      "id": "57a1eb00d85de250",
      "name": "Cannes",
      "place_type": "city",
      "url": "http://api.twitter.com/1/geo/id/57a1eb00d85de250.json"
    },
    "possibly_sensitive": false,
    "retweet_count": 57,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Photos on iOS</a>",
    "text": "Making us proud: @dickc at #CannesLions http://t.co/jv9NEXHH",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Tue Jun 19 22:58:12 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 215216944956182528,
    "id_str": "215216944956182528",
    "in_reply_to_screen_name": "JonVictorino",
    "in_reply_to_status_id": 215206191201132544,
    "in_reply_to_status_id_str": "215206191201132544",
    "in_reply_to_user_id": 74888746,
    "in_reply_to_user_id_str": "74888746",
    "place": null,
    "retweet_count": 1,
    "retweeted": false,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "text": "@JonVictorino no. That was fiction. And I didn't see it.",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Tue Jun 19 19:02:07 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 215157527858524160,
    "id_str": "215157527858524160",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 114,
    "retweeted": false,
    "source": "<a href=\"http://itunes.apple.com/us/app/snapseed/id439438619?mt=8&uo=4\" rel=\"nofollow\">Snapseed on iOS</a>",
    "text": "Sunset. http://t.co/hmseyMhr",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": {
      "coordinates": [
        7.01916,
        43.550694
      ],
      "type": "Point"
    },
    "created_at": "Tue Jun 19 15:28:03 +0000 2012",
    "favorited": false,
    "geo": {
      "coordinates": [
        43.550694,
        7.01916
      ],
      "type": "Point"
    },
    "id": 215103652879273984,
    "id_str": "215103652879273984",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": {
      "attributes": {},
      "bounding_box": {
        "coordinates": [
          [
            [
              6.944769,
              43.505012
            ],
            [
              7.074011,
              43.505012
            ],
            [
              7.074011,
              43.574785
            ],
            [
              6.944769,
              43.574785
            ]
          ]
        ],
        "type": "Polygon"
      },
      "country": "France",
      "country_code": "FR",
      "full_name": "Cannes, Alpes-Maritimes",
      "id": "57a1eb00d85de250",
      "name": "Cannes",
      "place_type": "city",
      "url": "http://api.twitter.com/1/geo/id/57a1eb00d85de250.json"
    },
    "possibly_sensitive": false,
    "retweet_count": 71,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Photos on iOS</a>",
    "text": "Hello, from #CannesLions. http://t.co/TLvbzYGL",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": {
      "coordinates": [
        -122.38975961,
        37.61179052
      ],
      "type": "Point"
    },
    "created_at": "Mon Jun 18 22:34:23 +0000 2012",
    "favorited": false,
    "geo": {
      "coordinates": [
        37.61179052,
        -122.38975961
      ],
      "type": "Point"
    },
    "id": 214848563472121856,
    "id_str": "214848563472121856",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": {
      "attributes": {},
      "bounding_box": {
        "coordinates": [
          [
            [
              -124.482003,
              32.528832
            ],
            [
              -114.131211,
              32.528832
            ],
            [
              -114.131211,
              42.009517
            ],
            [
              -124.482003,
              42.009517
            ]
          ]
        ],
        "type": "Polygon"
      },
      "country": "United States",
      "country_code": "US",
      "full_name": "California, US",
      "id": "fbd6d2f5a4e4a15e",
      "name": "California",
      "place_type": "admin",
      "url": "http://api.twitter.com/1/geo/id/fbd6d2f5a4e4a15e.json"
    },
    "retweet_count": 29,
    "retweeted": false,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "text": "Flying to Cannes for #CannesLions. First time in Southern France.",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 17 16:10:28 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 214389559721590784,
    "id_str": "214389559721590784",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "retweet_count": 29,
    "retweeted": false,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "text": "Watching #NASCAR Michigan. Rain, rain, go away.",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 17 04:01:27 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 214206090710237184,
    "id_str": "214206090710237184",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 273,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Photos on iOS</a>",
    "text": "Sunset. http://t.co/2mye8ZJJ",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 17 02:38:00 +0000 2012",
    "favorited": false,
    "geo": null,
    "id": 214185090283077632,
    "id_str": "214185090283077632",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 12,
    "retweeted": false,
    "source": "<a href=\"http://www.apple.com\" rel=\"nofollow\">Photos on iOS</a>",
    "text": "Mike Lewis. He doesn't approve. http://t.co/99BLwXyy",
    "truncated": false,
    "user": {
      "contributors_enabled": true,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Executive Chairman of Twitter, CEO of Square, a founder of both.",
      "favourites_count": 1047,
      "follow_request_sent": null,
      "followers_count": 2026995,
      "following": null,
      "friends_count": 1191,
      "geo_enabled": true,
      "id": 12,
      "id_str": "12",
      "is_translator": false,
      "lang": "en",
      "listed_count": 18038,
      "location": "San Francisco",
      "name": "Jack Dorsey",
      "notifications": null,
      "profile_background_color": "EBEBEB",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme7/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1563216547/image_normal.jpg",
      "profile_link_color": "990000",
      "profile_sidebar_border_color": "DFDFDF",
      "profile_sidebar_fill_color": "F3F3F3",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "jack",
      "show_all_inline_media": true,
      "statuses_count": 11242,
      "time_zone": "Pacific Time (US & Canada)",
      "url": null,
      "utc_offset": -28800,
      "verified": true
    }
  }
]

'''
