# GestureAssistant - Unleash the power of your hand and automate anything

## Inspiration
GestureAssistant  -  Unleash the power of your hand and automate anything 

## What it does
This is a simple prototype for GestureAssistant - a Desktop Personal Virtual Assistant which understands your gestures(so it understands you:) ) and turns them into powerful commands which will automate your Desktop without you lifting your finger..(but you will have to start the assistant yourself:))

It can automate almost anything that a computer can do..so it can do everything..

Scenario 1 : 
Lets say, your mom doesn't know how to operate a computer [I am sure there are lots of moms], and you are tired teaching them the same thing again and again.

I am in the same situation. And I applied my Engineering Brain to solve this problem.

 Scenario 2 : 
Suppose you are getting bored. You want to watch a movie on youtuve or listen to a song or send an email or play a game or chat with friends on facebook or peep into instagram or tweet on twitter or upload this code on Github:) or this or that and so on..............
Infinite scenarios...
But you dont want to go to your Start Menu --> Open Chrome --> enter the URL and wait for it to load..

One Solution...Gestures

Simply give a gesture command and get things done quickly...

## How I built it

Its built in python.
I have used Pytorch to recognize the hand gestures and then associated them with commands...
See github code for more details.

## Challenges I ran into
Started with deep learning for the first time...difficult to understand initially..but loved it after completion

## Accomplishments that I'm proud of
Built the app in 4 days ( and nights) !!!

## What I learned
Lot of things : 
1)How to use Pytorch with python
2)what is deep learning
3) How to automate things on Windows

## What's next for GestureAssistant - Your hand based Virtual Assistant
I would learn image processing using torchvision in depth to more accuretely analyze the gestures and add support for more gestures.


### Dataset
[Sign Language Dataset](https://www.kaggle.com/kumawatmanish/deep-learning-sign-language-dataset/data)

### File Description
- main.py
    - Entry point of the application for detecting sign language gesture
- collect_data.py
    - Entry point of the application for creating new sign language data

### Setup
Run the following command to install all required python packages
```console
pip install -r requirements.txt
```

### How to Detect Gesture
-Clone the github repo
-Install necessary packages
-Run main.py
-Wait for camera stream
-Place hand in 9 boxes to configure hand
-show gestures from 1,2,3,4,5 and observe the output


##### Instructions
- Place your hand on the screen around the green boxes as shown on the figure below
- Press 'z' button to start hand detection
- Press 'z' button once again to stop hand detection
- Press ESC button to exit the application

![Hand](https://res.cloudinary.com/practicaldev/image/fetch/s--iIEtBPzW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/aaijxoqwmrkyx8epxq4t.png "Hand Histogram")

