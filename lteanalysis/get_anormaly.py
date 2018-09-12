"""
必要モジュールロード
"""
# import sys
import time
from get_influencers import get_influencers
from change_path import change_path


"""
主処理
"""
def main():

	# host = sys.argv[1]
	# rt1 = sys.argv[2]
	# rt2 = sys.argv[3]
	host = '192.168.142.7:9200'
	rt1 = '192.168.3.253'
	rt2 = '192.168.3.252'
	password = "q"
	threshold  = 80

	anormaly = get_influencers(host)
	recent = anormaly["influencers"][0]["timestamp"]

	while True:

		anormaly = get_influencers(host)
		# import pdb; pdb.set_trace()


		if anormaly["count"] == 0: 
			time.sleep(1)
			continue

		if anormaly["influencers"][0]["timestamp"] == recent:
			time.sleep(1)
			continue

		if anormaly["influencers"][0]["influencer_score"] < threshold:
			time.sleep(1)
			continue

		recent = anormaly["influencers"][0]["timestamp"]
		anormaly_rt = anormaly["influencers"][0]["path.keyword"][22:35]
		# import pdb; pdb.set_trace()

		if anormaly_rt == rt1:
			time.sleep(1)
			change_path(rt2, rt1, password)
			continue

		if anormaly_rt == rt2:
			time.sleep(1)
			change_path(rt1, rt2, password)
			continue

		time.sleep(1)


"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
