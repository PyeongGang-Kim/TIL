데이터 셋을 불러오고 그 중에 아이리쉬 데이터 가져오기

```python
from sklearn import datasets
iris = datasets.load_iris()
print(iris.DESCR)
# DESCR은 상세 정보들 dict와 같은걸 보여줌
# .data를 사용하면 데이터만 나온다
# .feature_names를 사용하면 각 칼럼의 속성들이 나온다(꽃잎 길이, 너비 등)(헤드 태그와 비슷)
# .target은 그 데이터에 대한 분류(미리 정의해 놓은 종(숫자 값))을 받아온다.
# .target_names는 그 데이터에 대한 분류(미리 정의해 놓은 종(이름))을 받아온다.
```

기본 데이터 외에도 kaggle에 가면 데이터셋을 받아볼 수도 있다.

https://www.kaggle.com/datasets 

캘리포니아 대학, 어바인의 머신러닝 저장소

 https://archive.ics.uci.edu/ml/datasets 



활용 가능한 기본 정보

 https://datascienceschool.net/view-notebook/293ece8b0d124fbaa4d4d52bb8f1cb42/ 







직접 데이터셋 생성하기

선형 데이터 생성









```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
target = iris_dataset['target']    # label
# train/test 데이터 분리
train_input, test_input, train_label, test_label = train_test_split(iris_dataset['data'], target, test_size = 0.25, random_state=42)
# test_size: test data의 비율
# random_state: random seed 값

# 지도학습 모델 중 k-nn모델
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(train_input, train_label)    # 분류기 모델에 학습 데이터와 label 데이터 적용
predict_label = knn.predict(test_input)    # 분류기 모델의 결과 예측
import numpy as np
print('test accuracy {:.2f}'.format(np.mean(test_label == predict_label)))   # 정확도 출력 1
from sklearn.metrics import accuracy_score
print('test accuracy {:.2f}'.format(accuracy_score(test_label, predict_label)))    # 정확도 출력 2

# 비지도학습 모델 중 k-means 모델
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)
k_means.fit(train_input)
predict_cluster = k_means.predict(test_input)
print(predict_cluster)
# 단, 군집의 순서와 label의 값은 다를 수 있음, 예를 들어 0번째 군집에 라벨1인 데이터들이 주로 분포할 수 있음
print("0 cluster:", train_label[k_means.labels_ == 0])
print("1 cluster:", train_label[k_means.labels_ == 1])
print("2 cluster:", train_label[k_means.labels_ == 2])
```

