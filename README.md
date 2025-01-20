# earthquake_info
1s毎に最新の地震情報をパブリッシュするROS2のパッケージ \
タイムスタンプ・震源地・最大震度・震源に最も近い県名を取得し、ノードに流す。\
また、市名・マグニチュード・津波情報を追加で取得する

![test](https://github.com/HorigutiStudent/mypkg/actions/workflows/test.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) \
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">
## Requirements

- Linux OS
  - Ubuntu 22.04 
- ROS 2
  - Humble
- Python3
- [Earthquake_msg](https://github.com/HorigutiStudent/Earthquake_msg)
  - メッセージ型を定義したパッケージ
## Installation 
### Source Build
```sh
# ワークスペースの作成
mkdir ~/ros2_ws/src
#パッケージのダウンロード
cd ~/ros2_ws/src
git clone https://github.com/HorigutiStudent/Earthquake_Info.git
git clone https://github.com/HorigutiStudent/Earthquake_msg
#ライブラリのインストール
pip3 install requests
#パッケージのビルド
cd ~/ros2_ws
colcon build 
#セットアップ
source ~/ros2_ws/install/setup.bash
```
## Usage
### Quick Start
タイムスタンプ・震源地・最大震度・震源に最も近い県名を取得し、ノードに流す
```sh
cd ~/ros2_ws
source install/setup.bash 

ros2 run earthquake_info get_info 
#1: 2025-01-20T13:26:00+09:00, 石川県能登地方,1,石川県,none,0.0,none
```
### More Info
追加で市名・マグニチュード・津波情報を取得
```sh
#市名を追加で取得
ros2 run earthquake_info get_info --city True
#17: 2025-01-20T13:26:00+09:00, 石川県能登地方,1,石川県,志賀町,0.0,none

#マグニチュードを追加で取得
ros2 run earthquake_info get_info --magnitude True 
#21: 2025-01-20T13:26:00+09:00, 石川県能登地方,1,石川県,none,2.4000000953674316,none

#津波情報を追加で取得
ros2 run earthquake_info get_info --tunami True 
#30: 2025-01-20T13:26:00+09:00, 石川県能登地方,1,石川県,none,0.0,この地震による津波の心配はありません。

#3つとも追加で取得
ros2 run earthquake_info get_info --city True --magnitude True --tunami True 
#35: 2025-01-20T13:26:00+09:00, 石川県能登地方,1,石川県,志賀町,2.4000000953674316,この地震による津波の心配はありません。
```
## Nodes
- get_info
  - サイトから情報を取得するノード
- listener
  - テスト用ノード

## Tested
- Ubuntu 22.04
- Python 3.10
- ROS2 Humble 
  - Docker Container([ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2))
## License
- このソフトウェアパッケージは，MITライセンスの下，再頒布および使用が許可される. \
ライセンスの全文は[LICENSE](https://github.com/HorigutiStudent/mypkg/tree/dev?tab=License-1-ov-file)から確認できる.
- © 2025 Horiguchi Masahumi 