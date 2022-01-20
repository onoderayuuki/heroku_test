"""
    SVMアルゴリズムで手書き文字の判定を学習し、また結果を評価します.
"""
import os

if __name__ == "__main__":

    if not os.path.exists("result"):
        os.mkdir("result")

    """
        **** ここを実装します（基礎課題） ****
        `csv`フォルダからデータを読み込み、SVMアルゴリズムを用いた学習を行ってください。
        そして学習結果を`result`フォルダに`svm.pkl`という名前で保存してください。

        実装ステップ：
            ・トレーニングデータを読み込む
            ・SVGアルゴリズムによる学習を行う
            ・テストデータを読み込む
            ・精度とメトリクスによる性能評価を行う
            ・学習結果を`result/svm.pkl`ファイルとして保存する

        参考になる情報
            講義スライドや答えを適宜確認しながら実装してみてください。
            サンプルを見ながら手を動かしながら学ぶという感じがお勧めです。

        ここが一番大変なところです。
        ぜひぜひ頑張ってください！！
    """
#%%
from sklearn import svm
from sklearn import metrics

# training
#%%
with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")[:10000]
with open("./csv/train-labels.csv") as f:
    labels = f.read().split("\n")[:10000]
images = [[int(i)/256 for i in image.split(",")]for image in images]
labels = [int(l) for l in labels]
#%%
clf = svm.SVC()
clf.fit(images,labels)

# test
#%%
with open("./csv/test-images.csv") as f:
    images_test = f.read().split("\n")[:500]
with open("./csv/test-labels.csv") as f:
    labels_test = f.read().split("\n")[:500]

images_test = [[int(i)/256 for i in image.split(",")]for image in images_test]
labels_test = [int(l) for l in labels_test]
#%%
predict = clf.predict(images_test)
ac_score = metrics.accuracy_score(labels_test,predict)
print("Accuracy:",ac_score)
cl_report = metrics.classification_report(labels_test,predict)
print(cl_report)
# %%
# export model
import joblib
joblib.dump(clf, "./result/svm.pkl")
# %%
