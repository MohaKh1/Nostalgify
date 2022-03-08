import requests as rq
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = "8c2fc18077c54d7b8678b62e0d6958e4"
SPOTIFY_CLIENT_SECRET = "5744f9db3f10454cb2dda8ccb450b1ac"
SPOTIFY_USERNAME="MoHaKh"
ID="31ko3v7oai7eq4kmpsyv7obul4lm"
def spotify_auth():


    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()
    print(user_id)


def get_songs_and_artists(soup_site):
    top_song = soup_site.find(name="h3",
                                 class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
    top_song_artist = soup_site.find(name="span",
                                        class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").getText()
    top_song_artists = [top_song_artist.strip('\n')]
    top_99_artists = soup_site.find_all(name="span",
                                           class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
    top_100_songs = [top_song.getText().strip('\n')]
    top_99_songs = soup_site.find_all(name="h3",
                                         class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
    for i in range(len(top_99_songs)):
        temp_artist = top_99_artists[i].getText()
        temp = top_99_songs[i].getText()
        top_100_songs.append(temp.strip('\n'))
        top_song_artists.append(temp_artist.strip('\n'))
    print(top_100_songs)

    print(top_song_artists)


def scrape():
    print("Welcome to the Musical Wayback machine!\n")
    year = input("\nEnter the year you want to travel to 1950-2022: ")

    while int(year) not in range(1950, 2022):
        print("\n~IndexError: Invalid year entered.")
        year = input("\nEnter the year you want to travel to 1950-2022: ")

    user_date = year + "-" + "06-14/"


    music_chart_url = BILLBOARD_ENDPOINT + user_date
    print(music_chart_url)
    web_response = rq.get(url=music_chart_url)

    unscraped_webpage = web_response.text



    return BeautifulSoup(unscraped_webpage, "html.parser")



if __name__ == "__main__":
    # scraped_site = scrape()
    # get_songs_and_artists(scraped_site)
    spotify_auth()