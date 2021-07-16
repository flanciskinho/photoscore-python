import requests
from flask import Flask, request, render_template
from timeit import default_timer as timer
import concurrent.futures


app = Flask(__name__, static_folder='static', static_url_path='', template_folder='template')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return app.send_static_file('index.html')


def authenticate(username: str, password: str) -> str:
	payload: dict = {
		'username': username,
		'password': password
	}

	endpoint = 'https://api.photoilike.com/v2.0/authenticate'

	r = requests.post(endpoint, json=payload, timeout=5)

	return r.json()['id_token']


def get_score(session_token: str, client_key: str, url: str) -> dict:
	endpoint = 'https://api.photoilike.com/v2.0/score'

	headers = {
		'Authorization': 'Bearer ' + session_token,
	}

	payload = {
		'client-key': client_key,
		'image-url': url
	}

	r = requests.post(endpoint, headers=headers, json=payload, timeout=10)

	return {'url': url, 'score': r.json()['score']}


def get_scores(session_token: str, client_key: str, urls: list) -> list:
	result = []
	with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
		futures = [executor.submit(get_score, session_token, client_key, url) for url in urls]

		
		for future in concurrent.futures.as_completed(futures):
			try:
				result.append(future.result(10))
			except Exception as exc:
				print('generated exception: '.format(exc))

	return result



def parse_urls(session_token: str, client_key: str, urls: list, limit: int) -> dict:
	cnt = 0

	group = []
	result = []
	for url in urls.splitlines():
		if url.strip() == '':
			continue

		group.append(url)
		if len(group) == limit:
			result += get_scores(session_token, client_key, group);

			group = []
		cnt += 1

	group.append(url)
	if len(group) == limit:
		result += get_scores(session_token, client_key, group)

	return result



@app.route('/query', methods=['POST'])
def query():
	session_token = authenticate(request.form['user'], request.form['pass'])
	start_time = timer()
	results = parse_urls(session_token, request.form['client'], request.form['images'], 5)
	end_time = timer()

	execution_time = round(end_time - start_time, 2)

	return render_template('results.html', execution_time=str(execution_time), amount=len(results), results=results)

