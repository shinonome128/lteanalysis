"""
必要モジュールロード
"""
import telnetlib
import sys
from go_active import go_active
from go_standby import go_standby


"""
主処理
"""
def main():
 
	host1 = sys.argv[1]
	host2 = sys.argv[2]
	password = "q"

	change_path(host1, host2, password)


def change_path(host1, host2, password):

	go_standby(host2, password)
	go_active(host1, password)

	return


"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
