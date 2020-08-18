import os, glob,pathlib, os.path, sys 
import time, musicbrainzngs as mus 

mus.set_useragent("Private App", "0.2")
albumlist=[]
filepath = 'playlist.txt'
meklet = []


def get_cover(artist, album, size=500, retry_delay=5, retries=5):
    try:
        data = mus.search_releases(artist=artist,
                                   release=album,
                                   limit=1)
        #release_id = data["release-list"][0]["id"]
        release_id = data["release-list"][0]["release-group"]["id"]
        print(f"album: Using release-id: {data['release-list'][0]['id']}")

        return mus.get_release_group_image_front(release_id,None )

    except mus.NetworkError:
        if retries == 0:
            raise mus.NetworkError("Failure connecting to MusicBrainz.org")
        print(f"warning: Retrying download. {retries} retries left!")
        time.sleep(retry_delay)
        get_cover(song, size, retries=retries - 1)

    except mus.ResponseError:
        print("error: Couldn't find album art for")
    except:
        next




with open(filepath) as fp: 
    line = fp.readline()
    while line:
        line = fp.readline()
        
        meklet.append(line.strip())
infolist = []
albumold = ""
for k in meklet:
    try:
        artist, song  = k.split("-")
        #print(artist, song)
        rezult = mus.search_works(artist = artist, work = song, limit = 1)

        album = rezult["work-list"][0]["title"]
        print(album)
        data = mus.search_releases(artist=artist,
                                   release=album,
                                   limit=1)
        #print(data)
        release_date = data["release-list"][0]["release-event-list"][0]["date"]
        print(release_date[0:4])

        #infolist.append(artist+";"+album+";"+release_date[0:4])
        if album!=albumold:
            albumlist.append((artist, album))
            print("*")
        albumold = album
    except:
        next
#for n in infolist:
#    print(n)

albumlist = list(dict.fromkeys(albumlist))

for j in albumlist:
    print(j)
    artist, album = j
    print(artist +" "+album)
    album_art = get_cover(artist, album)
    if album_art!= None:
        filename = "images/" + artist + "-" + album + ".jpg"
        try:
            with open(filename, "wb") as file:
                file.write(album_art)
        except:
            next
