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

	go_standby(host, password)


"""
制御処理
"""
def go_standby(host, password):

	tn = telnetlib.Telnet(host)

	tn.read_until(b"Password:")
	tn.write(password.encode('ascii') + b"\n")

	tn.read_until(b">")
	tn.write(b"en\n")

	tn.read_until(b"Password:")
	tn.write(password.encode('ascii') + b"\n")

	
	tn.read_until(b"#")
	tn.write(b"conf t\n")

	tn.read_until(b"#")
	tn.write(b"interface Tunnel1\n")

	tn.read_until(b"#")
	tn.write(b"ip ospf cost 10000\n")

	tn.read_until(b"#")
	tn.write(b"interface GigabitEthernet0/0/0\n")

	tn.read_until(b"#")
	tn.write(b"ip ospf cost 10000\n")

	tn.read_until(b"#")
	tn.write(b"standby 5 priority 90\n")

	tn.read_until(b"#")
	tn.write(b"end\n")

	tn.read_until(b"#")
	tn.write(b"exit\n")

	return

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
