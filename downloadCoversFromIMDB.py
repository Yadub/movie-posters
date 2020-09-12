import urllib.request
from urllib.error import HTTPError
import pandas as pd
import socket


# Load file with Picture URLs for IPL photos
data_file_path = 'moviesAndCovers.csv'
df = pd.read_csv(data_file_path)
df.dropna(inplace=True)
# If downloading in parts then change start and max index for downloading images
start_index = 0
max_index = 10000
# Set dir where to save the photos
save_path_dir = './imbd_movie_covers/'
# Set timeout (seconds) incase there is a websocket timeout
webpage_timeout = 20
socket.setdefaulttimeout(webpage_timeout)
# Iterate
for i in df.index:
    if i < start_index: continue
    if i > max_index: break
    try:
        movie_name = df['Title'].loc[i]
        image_file_name = save_path_dir + 'img_' + movie_name + '.jpg'
        cover_url = df['Cover URL'].loc[i]
        urllib.request.urlretrieve(cover_url, image_file_name)
        print("Downloaded img at index: " + str(i) + " " + movie_name)
    except HTTPError as err:
        print("Failed for img at index " + str(i) + ". Due to HTTP error code: " + str(err.code) + " " + movie_name)
    except Exception as e:
        print("Failed for img at index " + str(i) + " " + movie_name)
        print(e)
