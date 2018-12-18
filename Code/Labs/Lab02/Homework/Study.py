# import to use youtube-dl
from youtube_dl import YoutubeDL

# 1. Download Video
# 1.1 Download a single youtube video
dl_vid = YoutubeDL()
dl_vid.download(['https://www.youtube.com/watch?v=cvaIgq5j2Q8'])
# 1.2 Download multiple youtube videos
dl_vids = YoutubeDL()
dl_vids.download(['https://www.youtube.com/watch?v=qgeaoW55Pks', 'https://www.youtube.com/watch?v=x9WpVoAC3tk'])

# 2. Download Audio
options1 = {
    'format': 'bestaudio/audio'
}
dl_aud = YoutubeDL(options1)
dl_aud.download(['https://www.youtube.com/watch?v=C76yS0OtJNA'])

# 3. Search and download videos
options2 = {
    'default_search': 'ytsearch',
}
dl_search_vid = YoutubeDL(options2)
dl_search_vid.download(['Cơn lốc trên đường cao tốc'])

# 4. Search and download audios
options3 = {
    'default_search': 'ytsearch',
    'format': 'bestaudio/audio'
}
dl_search_aud = YoutubeDL(options3)
dl_search_aud.download(['Daylight'])