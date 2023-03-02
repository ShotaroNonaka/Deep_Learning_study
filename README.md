# ニューラルネットワークの勉強用

## 目標
- 自分の研究をnnabla-rlでできるようにする
- XAIを導入する
  - tabularを扱えるlimeを勉強予定
    - 2023/2/28 limeの勉強
    - 2023/3/1  limeに関してまとめた
- 深層学習に詳しくなる
  - [pytorchチュートリアル](https://yutaroogawa.github.io/pytorch_tutorials_jp/)を勉強する
    - 2023/2/15 0章終わり
    - 2023/2/16 4章 深層強化学習(Reinforcement Learning) 終わり
    - 2023/2/17 2.1 転移学習 終わり
    - 2023/2/21 1章 PyTorch基礎(Learning PyTorch) 終わり
    - 2023/2/22 3章 自然言語処理 - TransformerとTorchTextを用いたsequence-to-sequenceモデルの学習 終わり
  - ~~書籍「[Pythonで学ぶ強化学習](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-Python%E3%81%A7%E5%AD%A6%E3%81%B6%E5%BC%B7%E5%8C%96%E5%AD%A6%E7%BF%92-%E6%94%B9%E8%A8%82%E7%AC%AC2%E7%89%88-%E5%85%A5%E9%96%80%E3%81%8B%E3%82%89%E5%AE%9F%E8%B7%B5%E3%81%BE%E3%81%A7-%E4%B9%85%E4%BF%9D/dp/4065172519/ref=sr_1_1?keywords=python%E3%81%A7%E5%AD%A6%E3%81%B6%E5%BC%B7%E5%8C%96%E5%AD%A6%E7%BF%92&qid=1676287990&sprefix=python%E3%81%A7%E5%AD%A6%E3%81%B6%2Caps%2C216&sr=8-1)」を再現する~~
  - 書籍「[ゼロからつくるＰｙｔｈｏｎ機械学習プログラミング入門](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E3%81%A4%E3%81%8F%E3%82%8B%EF%BC%B0%EF%BD%99%EF%BD%94%EF%BD%88%EF%BD%8F%EF%BD%8E%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%85%A5%E9%96%80-%EF%BC%AB%EF%BC%B3%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E5%85%AB%E8%B0%B7%E5%A4%A7%E5%B2%B3-ebook/dp/B08MF4BS7N/ref=sr_1_6?adgrpid=75531842116&gclid=CjwKCAiAr4GgBhBFEiwAgwORrdzwbzzML5LUeskb5nHrGD8MOVJv4r6N48tCKRp_KBbr-4LEQRNwNhoCYx4QAvD_BwE&hvadid=649708824170&hvdev=c&hvlocphy=1009543&hvnetw=g&hvqmt=e&hvrand=761601700493184354&hvtargid=kwd-851045153738&hydadcr=1798_13591159&jp-ad-ap=0&keywords=python+%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92+amazon&qid=1677749579&sr=8-6)」
    - こっちをpytorchとnnablaで再現する