# Edge Impulse: Time series data #

An accelerometer is a device that measures the vibration, or acceleration of motion of a structure. The force caused by vibration or a change in motion (acceleration) causes the mass to "squeeze" the piezoelectric material which produces an electrical charge that is proportional to the force exerted upon it. Since the charge is proportional to the force, and the mass is a constant, then the charge is also proportional to the acceleration.

## Start a project ##
 Select a name for your application, then choose "accelerometer data" and press the button "Let's get started". 
 ## Devices ###
 
Select "Use your mobile phone" and scan the QR code, then you can set the label and start reading data from your phone. You should record 30 samples at least to train a model. In this exercise, we are going to make two different movements One is shaking hands and the other is saying hello to someone who is far from us. If you want to avoid this step, you can use the dataset in this folder. Then select the option "Upload data". If you choose this option, the dataset is already divided into training and testing, so you need to select these options before choosing the files. 
 
 ## Data Acquisition ##
 
 You will see all the samples and can move forward to the next step. 
 
 ## Impulse Design ##
 
 This section is where the magic happens, we select our dataset, then the next block is spectral analysis (involves the calculation of waves or oscillations in a set of sequenced data), then select the objective, in this case, is Classification Finally, save the Impulse (model). 

### Create impulse ###
Brief information about the spectral analysis such as filters, frequency domain, spectral power, among others.

 ### Spectralfeatures ###
This section is focused on extracting features from the dataset.

### NN Classifier ###
We can start to train the model with the suggested setup
You can look that the model is quantized from float32 to int8.

## Retrain model ##
## Live Classification ## 
You can test how the model classifies one feature 

## Model Testing ##
The model will classify the testset.

## Deployment ##
Export the model to your phone to check if the inference can recognize between two movements.
 




 
 
