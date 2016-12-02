import requests
import pytesseract
index_url = 'http://210.35.251.243/reader/login.php'
login_url = 'http://210.35.251.243/reader/redr_verify.php'
capture_url = 'http://210.35.251.243/reader/captcha.php'

def download():
	response = requests.get(index_url)
	response.encoding = 'utf-8'
	return response.cookies
def capture(cookies):
	img = get-captcha(capture_url)
	img.save('capture_original.png')
	background = img.convert('l')
	background.save('capture_background.png')
	bw = background.point(lambda x :0 if x<1 else 255,'1')
	bw.save('capture_thresholded.png')
	return pytesseract.image_to_string(bw)

def login(user,password):
	cookies = download()
	code = capture()
	postdata = {
		'number':user,
		'password':password,
		'captcha':code,
		'select':'cert_no',
		'return_url':" " 
	}
	response = requests.post(url = login_url,cookies = cookies,date = postdata)
	response.encoding = 'utf-8'
	return response.text
