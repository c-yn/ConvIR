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
|Color|Model|Parameters|FLOPs|
|----|------|-----|-----|
|<font color=blue>Blue</font>|ConvIR-S (small)|5.53M|42.1G|
|<font color=red>Red</font>|ConvIR-B (base)| 8.63M|71.22G|
|<font color=black>Black</font>|ConvIR-L (large)| 14.83M |129.34G|

|Task|Dataset|PSNR|SSIM|
|----|------|-----|----|
|**Image Dehazing**|SOTS-Indoor|<font color=blue>41.53</font>/<font color=red>42.72</font>|<font color=blue>0.996</font>/<font color=red>0.997</font>|
||SOTS-Outdoor|<font color=blue>37.95</font>/<font color=red>39.42</font>|<font color=blue>0.994</font>/<font color=red>0.996</font>|
||Haze4K|<font color=blue>33.36</font>/<font color=red>34.15</font>/34.50|<font color=blue>0.99</font>/<font color=red>0.99</font>/0.99|
||Dense-Haze|<font color=blue>17.45</font>/<font color=red>16.86</font>|<font color=blue>0.648</font>/<font color=red>0.621</font>|
||NH-HAZE|<font color=blue>20.65</font>/<font color=red>20.66</font>|<font color=blue>0.807</font>/<font color=red>0.802</font>|
||O-HAZE|<font color=blue>25.25</font>/<font color=red>25.36</font>|<font color=blue>0.784</font>/<font color=red>0.780</font>|
||I-HAZE|<font color=blue>21.95</font>/<font color=red>22.44</font>|<font color=blue>0.888</font>/<font color=red>0.887</font>|
||SateHaze-1k-Thin/Moderate/Thick|<font color=blue>25.11</font>/<font color=blue>26.79</font>/<font color=blue>22.65</font>|<font color=blue>0.978</font>/<font color=blue>0.978</font>/<font color=blue>0.950</font>|
||NHR|<font color=blue>28.85</font>/<font color=red>29.49</font>|<font color=blue>0.981</font>/<font color=red>0.983</font>|
||GTA5|<font color=blue>31.68</font>/<font color=red>31.83</font>|<font color=blue>0.917</font>/<font color=red>0.921</font>|
|**Image Desnowing**|CSD|<font color=blue>38.43</font>/<font color=red>39.10</font>|<font color=blue>0.99</font>/<font color=red>0.99</font>|
||SRRS|<font color=blue>32.25</font>/<font color=red>32.39</font>|<font color=blue>0.98</font>/<font color=red>0.98</font>|
||Snow100K|<font color=blue>33.79</font>/<font color=red>33.92</font>|<font color=blue>0.95</font>/<font color=red>0.96</font>|
|**Image Deraining**|Test100|31.40|0.919|
||Test2800|33.73|0.937|
|**Defocus Deblurring**|DPDD|<font color=blue>26.06</font>/<font color=red>26.16</font>/<font color=black>26.36</font>|<font color=blue>0.810</font>/<font color=red>0.814</font>/<font color=black>0.820</font>|
|**Motion Deblurring**|GoPro|33.28|0.963|
||RSBlur|34.06|0.868|


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
