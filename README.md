# mypkg
1s毎に最新の地震情報をパブリッシュするROS2のパッケージ 

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

#パッケージのビルド
cd ~/ros2_ws
colcon build 
#セットアップ
source ~/ros2_ws/install/setup.bash
```
## Usage
### Quick Start
```sh
cd ~/ros2_ws
source install/setup.bash 
ros2 run earthquake_info get_info
```
より詳しい使い方はearchquake_infoのREADMEを参照してください
## Nodes
- get_info
  - サイトから情報を取得するノード
- listener
  - テスト用ノード

## Tested
- Ubuntu 22.04
- Python 3.10
## License
- このソフトウェアパッケージは，MITライセンスの下，再頒布および使用が許可される. \
ライセンスの全文は[LICENSE](https://github.com/HorigutiStudent/mypkg/tree/dev?tab=License-1-ov-file)から確認できる.
- © 2025 Horiguchi Masahumi 