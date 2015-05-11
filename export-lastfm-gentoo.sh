mv exported_tracks.txt exported_tracks_old.txt
rm exported_tracks.txt
python2.7 lastfm-export-scrobbles.py -u mb47
