import os
import sys

# This renames folders that have a year at the end and puts the year after
# the artist name so they are in chronological order

if len(sys.argv) > 1 and sys.argv[1] == "yes":
	print "GOING TO DO REAL RENAME"
else:
	print "DRY RUN - use second arg 'yes' to do it for real"

# traverse root directory, and get only directories 
for dir in os.listdir("."):
	if os.path.isdir(dir):
		last_four_chars = dir[-4:]		
		if last_four_chars.isdigit():
			first_hyphen_idx = dir.index(' - ')						
			artist = dir[:first_hyphen_idx]
			album = dir[first_hyphen_idx+3:-7]
			year = dir[-4:]
			if artist == "OST" or artist == "VA":
				# skip soundtracks and compilations
				continue
			#print "artist = {}".format(artist)
			#print "year = {}".format(year)
			#print "album = {}".format(album)
			new_folder = "{} - {} - {}".format(artist, year, album)
			print "{}".format(new_folder)
			if len(sys.argv) > 1 and sys.argv[1] == "yes":				
				os.rename(dir, new_folder)
			
