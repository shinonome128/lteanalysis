"""
必要モジュールロード
"""
import sys
import time
from datetime import datetime
from get_rssi import get_rssi


"""
主処理
"""
def main():

	host = sys.argv[1]
	password = "q"

	while True:

		file = open('rssi_' + host + '.log', 'a')

		date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		rssi = get_rssi(host, password)
		# import pdb; pdb.set_trace()
	
		file.write(date + ' ' + str(rssi) + '\n')
		file.close()

		time.sleep(1)


"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
