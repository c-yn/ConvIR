[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-sots-indoor)](https://paperswithcode.com/sota/image-dehazing-on-sots-indoor)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-sots-outdoor)](https://paperswithcode.com/sota/image-dehazing-on-sots-outdoor)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-haze4k)](https://paperswithcode.com/sota/image-dehazing-on-haze4k)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-i-haze)](https://paperswithcode.com/sota/image-dehazing-on-i-haze)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-o-haze)](https://paperswithcode.com/sota/image-dehazing-on-o-haze)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/snow-removal-on-snow100k)](https://paperswithcode.com/sota/snow-removal-on-snow100k)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/snow-removal-on-srrs)](https://paperswithcode.com/sota/snow-removal-on-srrs)


## Revitalizing Convolutional Network for Image Restoration

The official pytorch implementation of the paper **[Revitalizing Convolutional Network for Image Restoration
 (T-PAMI'24)](https://ieeexplore.ieee.org/abstract/document/10571568)**

#### Yuning Cui, Wenqi Ren, Xiaochun Cao, Alois Knoll

## Installation
The project is built with PyTorch 3.8, PyTorch 1.8.1. CUDA 10.2, cuDNN 7.6.5
For installing, follow these instructions:
~~~
conda install pytorch=1.8.1 torchvision=0.9.1 -c pytorch
pip install tensorboard einops scikit-image pytorch_msssim opencv-python
~~~
Install warmup scheduler:
~~~
cd pytorch-gradual-warmup-lr/
python setup.py install
cd ..
~~~
## Training and Evaluation
Please refer to respective directories.
## Results [Download]
|Model|Parameters|FLOPs|
|------|-----|-----|
|ConvIR-S (small)|5.53M|42.1G|
|ConvIR-B (base)| 8.63M|71.22G|
|ConvIR-L (large)| 14.83M |129.34G|



## Citation
~~~
@article{cui2024revitalizing,
  title={Revitalizing Convolutional Network for Image Restoration},
  author={Cui, Yuning and Ren, Wenqi and Cao, Xiaochun and Knoll, Alois},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2024},
  publisher={IEEE}
}

@inproceedings{cui2023irnext,
  title={IRNeXt: Rethinking Convolutional Network Design for Image Restoration},
  author={Cui, Yuning and Ren, Wenqi and Yang, Sining and Cao, Xiaochun and Knoll, Alois},
  booktitle={International Conference on Machine Learning},
  pages={6545--6564},
  year={2023},
  organization={PMLR}
}
~~~

## Contact
Should you have any problem, please contact Yuning Cui.
