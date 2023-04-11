## Chapter 5. 오차역전파법

| File | Description | Page |
| :-- | :-- | :-- |
| buy_apple_orange.py | Buying apple and orange example | 163 |
| layer_naive.py | Simple addition, multiplication layer | 161 |

### Concept
- 오차역전파법(backpropagation) : 각 노드의 미분을 뒤에서부터 구함. 변수의 오차를 더 빨리 구할 수 있다.
  - 덧셈, 뺄셈, ReLU, Sigmoid, Softmax-with-Loss, MSE, Affine층, Batch normalization, Weight decay 등 대부분이 가능하고 구현되어 있음.
- Softmax-with-Loss : 소프트맥스 계층과 교차 엔트로피를 합친 계층
  - Softmax-with-Loss와 MSE는 역전파가 $y_1 - t_1, y_2 - t_2, y_3 - t_3, ...$ 등 단순하게 표현된다. 각 오차가 의도적으로 그렇게 설계되었다.