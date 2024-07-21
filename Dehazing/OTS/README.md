### Download the Datasets
- reside-outdoor [[gdrive](https://drive.google.com/drive/folders/1eL4Qs-WNj7PzsKwDRsgUEzmysdjkRs22?usp=sharing)]
- (Separate SOTS test set if needed) [[gdrive](https://drive.google.com/file/d/16j2dwVIa9q_0RtpIXMzhu-7Q6dwz_D1N/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1R6qWri7sG1hC_Ifj-H6DOQ?pwd=o5sk)]


### Train on RESIDE-Outdoor
For example, train the small model
~~~
python main.py --mode train --data_dir your_path/reside-outdoor --version small
~~~

### Evaluation
Download model from [gdrive](https://drive.google.com/drive/folders/1_5fO2p5xoWO5cUEVoXJ7x3Uhg1AP18FQ?usp=sharing), [百度网盘](https://pan.baidu.com/s/1oYzdxs3FvLJMWx7S5GW0rA?pwd=dvta)

~~~
python main.py --mode test --data_dir your_path/reside-outdoor --test_model path_to_ots_model --version small
~~~

For training and testing, your directory structure should look like this

`Your path` <br/>
`├──reside-outdoor` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 