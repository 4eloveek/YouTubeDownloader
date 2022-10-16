from pytube import YouTube
lang=input('Put your lang/Выбери свой язык En/Ru ')
if lang == 'En' or lang == 'en':
	link = input('Enter URL of video')
	video = YouTube(link)
	print('Downloading...')
	stream = video.streams.get_highest_resolution()
	stream.download()
	print('Your video was downloaded to the script folder')
else:
	link = input('Введи ссылку на видео ')
	video = YouTube(link)
	print('Скачивание...')
	stream = video.streams.get_highest_resolution()
	stream.download()
	print('Видео скачалось в папку со скриптом')