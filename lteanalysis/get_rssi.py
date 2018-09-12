"""
必要モジュールロード
"""
import telnetlib
import sys


"""
主処理
"""
def main():
 
	host = sys.argv[1]
	password = "q"

	print(get_rssi(host, password))


"""
電界強度取得処理
"""
def get_rssi(host, password):

	tn = telnetlib.Telnet(host)
	 
	tn.read_until(b"Password:")
	tn.write(password.encode('ascii') + b"\n")

	tn.read_until(b">")
	tn.write(b"en\n")

	tn.read_until(b"Password:")
	tn.write(password.encode('ascii') + b"\n")

	 
	tn.read_until(b"#")
	tn.write(b"show cellular 0/1/0 radio | i RSSI\n")

	result = str(tn.read_until(b"#"))
	tn.write(b"exit\n")

	line = result.split("\\r\\n")[1]
	# import pdb; pdb.set_trace()

	rssi = int(line.split(" ")[3])
	# import pdb; pdb.set_trace()

	return rssi

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
