### Download the dataset and model

[training_rainy](https://drive.google.com/file/d/1zmT3EuYAKfqiLlrnAz5SrOyuEHl52M71/view?usp=sharing)
[training_gt](https://drive.google.com/file/d/1unbTfkL3hhWtiwL27_ipLkPMC-aW3Ifc/view?usp=drive_link)
[testset](https://drive.google.com/file/d/1Tmz96YWtiBcA_mEu6Jrmp2R86j2g6Mfp/view?usp=drive_link)
model: [gdrive](https://drive.google.com/drive/folders/1_5fO2p5xoWO5cUEVoXJ7x3Uhg1AP18FQ?usp=sharing), [百度网盘](https://pan.baidu.com/s/1oYzdxs3FvLJMWx7S5GW0rA?pwd=dvta)


### Training

After setting the data_dir and valid_data in ``main.py``, then run

~~~
python main.py
~~~

### Testing
After setting the data_dir and test_model in ``test.py``, then run
~~~
python test.py
~~~

By doing this, the resulting images will be saved.
Next, run the matlab file to get the scores.


