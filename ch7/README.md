## Chapter 7. 합성곱 신경망

| File | Description | Page |
| :-- | :-- | :-- |
| params.pkl | Trained convnet model parameter | 00 |
| simple_convnet.py | Simple convnet model | 00 |
| train_convnet.py | Train convnet model | 00 |
| visualize_filter.py | Visualize convnet's 2d array filter | 00 |

### Concept
- 기존의 완전연결 신경망 : Affine-ReLU - Affine-ReLU - ...
  - 한계 : 데이터의 형상이 무시됨
- CNN(Convolution Neural Network, 함성곱 신경망) : Conv-ReLU-Pooling - Conv-ReLU-Pooling - ...

- feature map(특징맵) : IO data from CNN layers
  - input feature map : input data
  - output feature map : output data

- convolution
  - Fused multiply-add(FMA, 단일 곱셈 누산) : multiply and sum all
- convolution : FMA with sliding window based on the image
  - Window, kernel, filter : multiplied mask
  - Padding : filled value at the edge of image
  - Stride : sliding amount
  - Pooling : shrink the image

- im2col : Convolution의 연산 속도를 높이기 위해 객체를 2차원 배열로 변환
- col2im : 2차원 배열을 원래 형상의 텐서로 변환