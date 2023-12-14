import os

#Change the parameters as requirement

src_aud = "youtube-music"  # ["youtube","youtube-music","slider-kz"]
format_type = "flac"  # ["flac","m4a","ogg","mp3","opus","wav"]
bitrate = "320k"  # ["auto","disable","8k","16k","24k","32k","40k","48k","64k","80k","96k","112k","128k","160k","192k","224k","256k","320k"]
generate_lrc = False
lyrics = "musixmatch"  # ["genius","musixmatch","azlyrics","synced"]

output_directory = r"G:\Python Codes\Spotify\Downloaded Music"  #Add the path of Desired Directory

while True:
    spotify_url = input("Enter the Spotify URL (or 'exit' to stop): ")
    
    if spotify_url.lower() == 'exit':
        break

    if generate_lrc:
        print('\033[92mDownloading song from Spotify\033[0m\n')
        os.chdir(output_directory)
        os.system(f'spotdl {spotify_url} --audio {src_aud} --format {format_type} --lyrics {lyrics} --bitrate {bitrate}')
        print('\n\033[93mREAD:\033[0m \033[1mDownloaded song is located in your output directory.\033[0m')
    else:
        print('\033[92mDownloading song from Spotify\033[0m\n')
        os.chdir(output_directory)
        os.system(f'spotdl {spotify_url} --audio {src_aud} --format {format_type} --lyrics {lyrics} --bitrate {bitrate}')
        print('\n\033[93mREAD:\033[0m \033[1mDownloaded song is located in your output directory.\033[0m')

        