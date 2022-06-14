# s3
Programs to access objects in s3 storage.

See the python examples for any required environment variables.

Dev Environment

```
$ python --version
Python 3.9.12
```

Install and Test

```
python3 -m venv ~/tmpenv
source ~/tmpenv/bin/activate
pip install pip -qU    
pip install -qr requirements.txt 
python get-protobuf-s3.py 
```

Expected Output
```
INFO:root:Tensorflow version: 2.9.1
2022-05-27 16:25:15.040980: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:Inconsistent references when loading the checkpoint into this object graph. For example, in the saved checkpoint object, `model.layer.weight` and `model.layer_copy.weight` reference the same variable, while in the current object these are two different variables. The referenced variables are:(<keras.saving.saved_model.load.TensorFlowTransform>TransformFeaturesLayer object at 0x1276603a0> and <keras.engine.input_layer.InputLayer object at 0x1275c7940>).
WARNING:tensorflow:Inconsistent references when loading the checkpoint into this object graph. For example, in the saved checkpoint object, `model.layer.weight` and `model.layer_copy.weight` reference the same variable, while in the current object these are two different variables. The referenced variables are:(<keras.saving.saved_model.load.TensorFlowTransform>TransformFeaturesLayer object at 0x1276603a0> and <keras.engine.input_layer.InputLayer object at 0x1275c7940>).
Model: "model"
__________________________________________________________________________________________________
 Layer (type)                   Output Shape         Param #     Connected to                     
==================================================================================================
 HR_xf (InputLayer)             [(None, 1)]          0           []                               
                                                                                                  
 Resp_xf (InputLayer)           [(None, 1)]          0           []                               
                                                                                                  
 Temp_xf (InputLayer)           [(None, 1)]          0           []                               
                                                                                                  
 concatenate (Concatenate)      (None, 3)            0           ['HR_xf[0][0]',                  
                                                                  'Resp_xf[0][0]',                
                                                                  'Temp_xf[0][0]']                
                                                                                                  
 dense (Dense)                  (None, 100)          400         ['concatenate[0][0]']            
                                                                                                  
 dense_1 (Dense)                (None, 70)           7070        ['dense[0][0]']                  
                                                                                                  
 dense_2 (Dense)                (None, 50)           3550        ['dense_1[0][0]']                
                                                                                                  
 dense_3 (Dense)                (None, 20)           1020        ['dense_2[0][0]']                
                                                                                                  
 dense_4 (Dense)                (None, 1)            21          ['dense_3[0][0]']                
                                                                                                  
 transform_features_layer (Tens  multiple            0           []                               
 orFlowTransform>TransformFeatu                                                                   
 resLayer)                                                                                        
                                                                                                  
==================================================================================================
Total params: 12,061
Trainable params: 12,061
Non-trainable params: 0
__________________________________________________________________________________________________
INFO:root:Input: [-0.060083888471126556, -0.9738271832466125, 1.370796918869]: Prediction: [[-35.60883]]
INFO:root:Input: [0.060083888471126556, 0.9738271832466125, 1.01]: Prediction: [[1.7196066]]
INFO:root:Input: [0.2, 0.1, 1]: Prediction: [[-9.383452]]
```

