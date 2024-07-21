### Download the Datasets
- SRRS [[gdrive](https://drive.google.com/file/d/11h1cZ0NXx6ev35cl5NKOAL3PCgLlWUl2/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1VXqsamkl12fPsI1Qek97TQ?pwd=vcfg)]
- CSD [[gdrive](https://drive.google.com/file/d/1pns-7uWy-0SamxjA40qOCkkhSu7o7ULb/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1N52Jnx0co9udJeYrbd3blA?pwd=sb4a)]
- Snow100K [[gdrive](https://drive.google.com/file/d/19zJs0cJ6F3G3IlDHLU2BO7nHnCTMNrIS/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1QGd5z9uM6vBKPnD5d7jQmA?pwd=aph4)]

### Training
 version=small/base/large for different versions
~~~
python main.py --data CSD --version small --mode train --data_dir your_path/CSD
python main.py --data SRRS --version small --mode train --data_dir your_path/SRRS
python main.py --data Snow100K --version small --mode train --data_dir your_path/Snow100K
~~~

### Evaluation
#### Download the model
[gdrive](https://drive.google.com/drive/folders/1_5fO2p5xoWO5cUEVoXJ7x3Uhg1AP18FQ?usp=sharing), [百度网盘](https://pan.baidu.com/s/1oYzdxs3FvLJMWx7S5GW0rA?pwd=dvta)
#### Testing
 version=small/base/large for different versions
~~~
python main.py --data CSD --version small --save_image True --mode test --data_dir your_path/CSD --test_model path_to_CSD_model

python main.py --data SRRS --version small --save_image True --mode test --data_dir your_path/SRRS --test_model path_to_SRRS_model

python main.py --data Snow100K --version small --save_image True --mode test --data_dir your_path/Snow100K --test_model path_to_Snow100K_model
~~~


For training and testing, your directory structure should look like this

`Your path` <br/>
 `├──CSD` <br/>
     `├──train2500`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
     `└──test2000`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
 `├──SRRS` <br/>
     `├──train2500`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
     `└──test2000`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
 `└──Snow100K` <br/>
     `├──train2500`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
     `└──test2000`  <br/>
          `├──Gt`  <br/>
          `└──Snow`  
