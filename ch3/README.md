## Chapter 3. 신경망

| File | Description | Page |
| :-- |:--   |:--      |
| active_function.py | active function example | 68 |
| output_layer.py | identity function, softmax function | 91 |

### Concept
- 출력층
  - identity function (generally used in regression)
  - softmax function (generally used in classification)
    - 원래는 $$\frac{exp(a_k)}{\sum_{i=1}^{n}exp(a_i)}$$이지만, overflow 방지를 위해 $$\frac{exp(a_k - C)}{\sum_{i=1}^{n} exp(a_i - C)}$$ (C는 신호 중 최댓값)을 사용한다.
    - 보통 학습 단계에서는 softmax function을 사용하고, 추론 단계에서는 softmax function을 생략한다.
- one-hot encoding : result label : 7 <=> [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
- np.sum 인자 axis=i : i번째 차원을 구성하는 각 원소의 합
- np.argmax 인자 axis=i : i번째 차원을 구성하는 각 원소 중 최댓값의 인덱스
- 입력 데이터를 묶은 것을 batch라 한다. 결과를 빠르게 얻을 수 있다.