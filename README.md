# Filament-Tube-Clock
Filament Tube Clock. Developing with microPython or C.2022/10~

## 手順

1. 時計を作る
   1. 構造を調べてデータに起こす
   2. 再加工可能な状態でケースを設計する
   3. ケースを作成する
2. wifiモジュールをテストする
3. マイコンのテストをする。(同じピン配置の方がいいため)
4. 作り変える。

まずはmicroPythonで作成します。その後，Cで書き直す可能性があります。

## 回路

watch.pdfを参照。
基板データは非公開。

## 加工

[onshape](https://cad.onshape.com/documents/2ef8b39e419f2c465de1c02f/w/79a8761cf37ad37e1899c9b7/e/8a61e6004c59a43205288173?renderMode=0&uiState=6300f7f17d54bd0869f3cc04)

## 部品

|NAME|Quantity|memo|URL|
|----|--------|----|---|
|Raspberry Pi Pico|1||https://akizukidenshi.com/catalog/g/gM-16132/|
|IV-9 |6|フィラメント菅|https://nixie-tube.com/shop/1_76.html|
|5V2A|1|1Aで十分|https://akizukidenshi.com/catalog/g/gM-01801/|
|DCジャック|1|2.1mm|https://akizukidenshi.com/catalog/g/gC-09408/|
|タクトスイッチ|4|色は何でも|https://akizukidenshi.com/catalog/g/gP-03647/|
|M3ねじ||||
|配線用リール||||
|ボタン電池|1|1.5V|https://www.amazon.co.jp/dp/B003X5WJR6?tag=amz-mkt-edg-jp-22|
|電池ホルダ(LR44用)|1||https://akizukidenshi.com/catalog/g/gP-08208/|
|ICソケット18pin|1||https://akizukidenshi.com/catalog/g/gP-00008/|
|ICソケット8pin|1||https://akizukidenshi.com/catalog/g/gP-00017/|
|ICソケット28pin|3||https://akizukidenshi.com/catalog/g/gP-00013/|
|||||
|DS1307+|1|RTC(タイムキーパー)|https://akizukidenshi.com/catalog/g/gI-06949/|
|MCP23017|3|I/Oエキスパンダー|https://akizukidenshi.com/catalog/g/gI-09486/|
|水晶発振子32.768kHz|1||https://akizukidenshi.com/catalog/g/gP-04005/|
|10kΩ|5||https://akizukidenshi.com/catalog/g/gR-25103/|
|1kΩ|2|I2Cバス用|https://akizukidenshi.com/catalog/g/gR-25102/|
|15Ω|6||https://akizukidenshi.com/catalog/g/gR-09429/|
|0.1µF|6||https://akizukidenshi.com/catalog/g/gP-00090/|
|ＧＰＳ受信機キット　１ＰＰＳ出力付き　「みちびき」|1||https://akizukidenshi.com/catalog/g/gK-09991/|

# OSS

本プロジェクトで使用している"ds1307.py"は下記から利用しています。Thank you so much for your excellent work!!

>MicroPython TinyRTC I2C Module, DS1307 RTC + AT24C32N EEPROM
>https://github.com/mcauser/micropython-tinyrtc
>
>MIT License
>Copyright (c) 2018 Mike Causer

# GPSに関して

[ＧＰＳ受信機](https://akizukidenshi.com/catalog/g/gK-09991/)はMiniGPSを使用して設定を下記に変更する。

- baudrate=115200
- GPZDAのみ
- 更新周期はお好みで。5Hzか10Hzくらいでしょうか。