### Download the Datasets
- reside-indoor [[gdrive](https://drive.google.com/drive/folders/1pbtfTp29j7Ip-mRzDpMpyopCfXd-ZJhC?usp=sharing), [Baidu](https://pan.baidu.com/s/1jD-TU0wdtSoEb4ki-Cut2A?pwd=1lr0)]
- (Separate SOTS test set if needed) [[gdrive](https://drive.google.com/file/d/16j2dwVIa9q_0RtpIXMzhu-7Q6dwz_D1N/view?usp=sharing), [Baidu](https://pan.baidu.com/s/1R6qWri7sG1hC_Ifj-H6DOQ?pwd=o5sk)]


### Training
on ITS
~~~
python main.py 
--mode train 
--version small
--data ITS 
--data_dir your_path/reside-indoor 
--batch_size 4
--learning_rate 1e-4
--num_epoch 1000
--save_freq 20
--valid_freq 20
~~~

To train on real haze or haze4k, please uncomment the corresponding hyper-parameter part

Then run ``python main.py --data Haze4K`` or ``python main.py --data real_haze`` with the mode and model version you want, such as small/large.

Please comfirm that the model is trained on a larger patch for real haze.
### Evaluation
Download model from [gdrive](https://drive.google.com/drive/folders/1_5fO2p5xoWO5cUEVoXJ7x3Uhg1AP18FQ?usp=sharing), [百度网盘](https://pan.baidu.com/s/1oYzdxs3FvLJMWx7S5GW0rA?pwd=dvta)
#### Testing
~~~
python main.py 
--mode test 
--data_dir your_path/reside-indoor 
--test_model path_to_its_model 
--data ITS
~~~


For training and testing, your directory structure should look like this

`Your path` <br/>
`├──reside-indoor` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
          
`└──NHR` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 
          
`└──GTA5` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 
          
`└──haze4k` <br/>
     `├──train`  <br/>
          `├──GT`  <br/>
          `└──IN`  
     `└──test`  <br/>
          `├──GT`  <br/>
          `└──IN` 
          
`└──Haze1k-thin` <br/>
     `├──train`  <br/>
          `├──input`  <br/>
          `└──target`  
     `└──test`  <br/>
          `├──input`  <br/>
          `└──target` 
          
`└──Haze1k-moderate` <br/>
     `├──train`  <br/>
          `├──input`  <br/>
          `└──target`  
     `└──test`  <br/>
          `├──input`  <br/>
          `└──target` 
          
`└──Haze1k-thick` <br/>
     `├──train`  <br/>
          `├──input`  <br/>
          `└──target`  
     `└──test`  <br/>
          `├──input`  <br/>
          `└──target` 
          
`└──Dense-Haze` <br/>
     `├──train`  <br/>
          `├──hazy`  <br/>
          `└──gt`  
     `└──test`  <br/>
          `├──hazy`  <br/>
          `└──gt` 
