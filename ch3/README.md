## Chapter 1. 헬로 파이썬

| No | File | Description |
| :-- |:--   |:--      |
| active_function.py | active function example | 91 |
| MLP.py | 3 layered MLP example | 

### Concept
- 출력층
  - identity function (generally used in regression)
  - softmax function (generally used in classification)
    - 원래는 $$\frac{exp(a_k)}{\sum_{i=1}^{n}exp(a_i)}$$이지만, overflow 방지를 위해 $$\frac{exp(a_k - C)}{\sum_{i=1}^{n} exp(a_i - C)}$$ (C는 신호 중 최댓값)을 사용한다.
    - 보통 학습 단계에서는 softmax function을 사용하고, 추론 단계에서는 softmax function을 생략한다.