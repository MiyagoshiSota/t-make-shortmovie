from pathlib import Path
from openai import OpenAI

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(model="tts-1", voice="alloy", input="")

response.stream_to_file(speech_file_path)

# "課題(7章):受験レビュー|AIT Moodle R6開始日時 2024年07月18日(木曜日) 19:00状態終了完了日時 2024年07月18日(木曜日) 19:28所要時間27分15秒問題1 画素の輝度値が16ビットの場合、最大の輝度値は 65535(あってる) になる問題2 グレースケール画像の場合、輝度値が最大である画素は白色(あってる)になり、輝度値が最小である画素は黒色(あってる)になる。問題3 Prewittフィルタにおいて、フィルタの各要素の値を3で割る理由は 生成される画像の輝度値が許される最大値より大きくならないため(あってる) 問題4 輝度値がRGBであるカラー画像から輪郭を抽出するためにフィルタリングする場合、選択肢2(あってる) 選択肢1: カラー画像に対して1回だけフィルタリングを行う。選択肢2:各RGB成分に対して同じフィルタでフィルタリングを行う。選択肢3:各RGB成分に対して異なるフィルタでフィルタリングを行う。選択肢4:3つの異なるフィルタを合成した後、カラー画像に対して1回だけフィルタリングを行う。問題5 プーリング層の役割は データを小さくすること(あってる)である 問題6 部分的に正解畳み込み演算の問題である。スライド2ページの畳み込みを計算すると 12 (ちがってる) となる、スライド3ページの畳み込みを計算すると17(ちがってる) となる、スライド4ページの畳み込みを計算すると 13(ちがってる) となる、スライド5ページの畳み込みを計算すると 15(あってる) となる。"
