[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-sots-indoor)](https://paperswithcode.com/sota/image-dehazing-on-sots-indoor)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-sots-outdoor)](https://paperswithcode.com/sota/image-dehazing-on-sots-outdoor)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-haze4k)](https://paperswithcode.com/sota/image-dehazing-on-haze4k)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-i-haze)](https://paperswithcode.com/sota/image-dehazing-on-i-haze)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/image-dehazing-on-o-haze)](https://paperswithcode.com/sota/image-dehazing-on-o-haze)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/snow-removal-on-snow100k)](https://paperswithcode.com/sota/snow-removal-on-snow100k)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revitalizing-convolutional-network-for-image/snow-removal-on-srrs)](https://paperswithcode.com/sota/snow-removal-on-srrs)


## Revitalizing Convolutional Network for Image Restoration

The official pytorch implementation of the paper **[Revitalizing Convolutional Network for Image Restoration](https://ieeexplore.ieee.org/abstract/document/10571568)**

#### Yuning Cui, Wenqi Ren, Xiaochun Cao, Alois Knoll

## News
All resulting images and pre-trained models are available in the provided links.

**11/26/2024** Code for real haze and haze4k are released.

**07/22/2024** We release the code for dehazing (ITS/OTS), desnowing, deraining, and motion deblurring.

## Pretrained models
[gdrive](https://drive.google.com/drive/folders/1_5fO2p5xoWO5cUEVoXJ7x3Uhg1AP18FQ?usp=sharing), [百度网盘](https://pan.baidu.com/s/1oYzdxs3FvLJMWx7S5GW0rA?pwd=dvta)


## Installation
The project is built with PyTorch 3.8, PyTorch 1.8.1. CUDA 10.2, cuDNN 7.6.5
For installing, follow these instructions:
~~~
conda install pytorch=1.8.1 torchvision=0.9.1 -c pytorch
pip install tensorboard einops scikit-image pytorch_msssim opencv-python
~~~

*Please use the pillow package downloaded by Conda rather than pip.*



Install warmup scheduler:
~~~
cd pytorch-gradual-warmup-lr/
python setup.py install
cd ..
~~~
## Training and Evaluation
Please refer to respective directories.
## Results 
### Visualization Results: [gdrive](https://drive.google.com/drive/folders/1YiuiYG36zqgHsoUhbk6UJAAywGc0avnj?usp=sharing), [百度网盘](https://pan.baidu.com/s/1mDlRfEoMSi8vpCLRUxk2tQ?pwd=y2gv)
|Model|Parameters|FLOPs|
|------|-----|-----|
|*ConvIR-S (small)*|5.53M|42.1G|
|**ConvIR-B (base)**| 8.63M|71.22G|
|<ins>ConvIR-L (large)</ins>| 14.83M |129.34G|

|Task|Dataset|PSNR|SSIM|
|----|------|-----|----|
|**Image Dehazing**|SOTS-Indoor|*41.53*/**42.72**|*0.996*/**0.997**|
||SOTS-Outdoor|*37.95*/**39.42**|*0.994*/**0.996**|
||Haze4K|*33.36*</font>/**34.15**/<ins>34.50</ins>|*0.99*/**0.99**/<ins>0.99</ins>|
||Dense-Haze|*17.45*/**16.86**|*0.648*/**0.621**|
||NH-HAZE|*20.65*/**20.66**|*0.807*/**0.802**|
||O-HAZE|*25.25*/**25.36**|*0.784*/**0.780**|
||I-HAZE|*21.95*/**22.44**|*0.888*/**0.887**|
||SateHaze-1k-Thin/Moderate/Thick|*25.11*/*26.79*/*22.65*|*0.978*/*0.978*/*0.950*|
||NHR|*28.85*/**29.49**|*0.981*/**0.983**|
||GTA5|*31.68*/**31.83**|*0.917*/**0.921**|
|**Image Desnowing**|CSD|*38.43*/**39.10**|*0.99*/**0.99**|
||SRRS|*32.25*/**32.39**|*0.98*/**0.98**|
||Snow100K|*33.79*/**33.92**|*0.95*/**0.96**|
|**Image Deraining**|Test100|<ins>31.40</u>|<ins>0.919</ins>|
||Test2800|<ins>33.73</ins>|<ins>0.937</ins>|
|**Defocus Deblurring**|DPDD|*26.06*/**26.16**/<ins>26.36</ins>|*0.810*/**0.814**/<ins>0.820</ins>|
|**Motion Deblurring**|GoPro|<ins>33.28</ins>|<ins>0.963</ins>|
||RSBlur|<ins>34.06</ins>|<ins>0.868</ins>|


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
