# lteanalysis  
  
## 目的  
  
LTEルータの電界強度が場所により不安定  
閾値での監視が困難、データから相関と周期を学習して自動的に切り替える  
  
## 参照先  
  
なし  
  
## 構成  
  
### 物理・論理構成  
  
![物理・論理構成](https://drive.google.com/uc?export=view&id=1sCdxmneERVtnAQojz3sYBRQFGiKRh1rU)  
  
### システム構成  
  
![システム構成](https://drive.google.com/uc?export=view&id=1qa_JeD4BJ9KrSQt1zzIgWfxNz-Lxzphn)  
  
## モジュール説明  
  
ディレクトリ配置  
```  
.\lteanalysis\elasticsearch\elasticsearch.yml  
.\lteanalysis\kibana\export.json  
.\lteanalysis\kibana\kibana.yml  
.\lteanalysis\lteanalysis\change_path.py  
.\lteanalysis\lteanalysis\get_anormaly.py  
.\lteanalysis\lteanalysis\get_influencers.py  
.\lteanalysis\lteanalysis\get_log.py  
.\lteanalysis\lteanalysis\get_rssi.py  
.\lteanalysis\lteanalysis\go_active.py  
.\lteanalysis\lteanalysis\go_standby.py  
.\lteanalysis\logstash\logstash.conf  
.\lteanalysis\logstash\logstash.yml  
.\lteanalysis\packetbeat\packetbeat.yml  
.\lteanalysis\xpacml\rssi.json  
```  
  
logstash.yml  
logstash 設定ファイル  
  
logstash.conf  
syslog, 電界強度をELT  
syslog を受信  
syslog を elasticsearch に送信  
電界強度を elasticsearch に送信  
  
elasticsearch.yml  
elasticsearch 設定  
  
export.json  
kibana ダッシュボード設定  
  
kibana.yml  
kibana 設定  
  
rssi.json  
x-pac 機械学習モジュール設定  
  
packetbeat.yml  
死活監視  
ICMP結果を elasticsearch に送信  
  
change_path.py  
待機系・主系切り替え  
  
go_active.py  
主系切り替え  
  
go_standby.py  
待機系切り替え  
  
get_log.py  
電界強度を取得  
  
get_influencers.py  
異常検知イベント取得  
  
get_anormaly.py  
異常判定ロジック  
  
get_rssi.py  
電界強度を取得  
  
DOCOMO-LTE.txt  
拠点ルータ設定  
  
KDDI-LTE.txt  
拠点ルータ設定  
  
DC.txt  
センタルータ設定  
  
以上  
