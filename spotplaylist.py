import sys
import spotipy
import spotipy.util as util

artistasFile = open('artistas.txt', 'r')
artista = [x.strip('\n') for x in artistasFile.readlines()]

tracks = []

numeroArtistas = len(artista)

username = 'Gustavo Sanches'
scope = 'playlist-modify-public'
playlist_id = '5Rv3y6pFeTdt2DMVVr5pRN'


token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id='544d8f3b061840438390408c9dd24cb9',
                                   client_secret='7m7qqbmevw6Q7NWJ9nIhcf',
                                   redirect_uri='http://localhost:8888/callback')


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0, numeroArtistas):
        result = sp.search(artista[x], limit=5)
        for i, t in enumerate(result['tracks']['items']):
            tracks.append(str(t['id'].strip( 'u' )))
            print("adicionando a track", t['id'], t['name'])
    while tracks:
        try:
            result = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1])
        except:
            print("erro")
        tracks = tracks[1:]
    
else:
    print("Can't get token for", username)