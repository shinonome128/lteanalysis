"""
必要モジュールロード
"""
# import sys
import requests
import json

"""
主処理
"""
def main():
 
	# host = sys.argv[1]
	host = '192.168.142.7:9200'

	print(get_influencers(host))


"""
インフルエンサー取得処理
"""
def get_influencers(host):

	api = '/_xpack/ml/anomaly_detectors/rssi/results/influencers'
	url = 'http://'+ host + api
	headers = {'content-type': 'application/json'}

	payload = {'sort' : 'timestamp',
		'desc' : True,
		'start' : 'now-3000m'}
	#import pdb; pdb.set_trace()

	r = requests.get(
		url, 
		data = json.dumps(payload),
		headers = headers)
	# import pdb; pdb.set_trace()

	influencers = r.json()
	# import pdb; pdb.set_trace()
	# print(json.dumps(influencers, indent=4))


	return influencers

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
