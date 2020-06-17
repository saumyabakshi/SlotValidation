# SlotValidation

Assumptions : 

1.For finite entity post api, if pick_first is true then first element is picked else the logic works on default values of supported_multiple true and pick_first false.

2.I have allowed duplicate slot values to be processed.

3.For the numeric entity post api, if pick_first is true then first element is picked else the logic works on default values of supported_multiple true and pick_first false. In case of no constraint and no value , Ive returned the response as expected by 'no value' condition.

Docker:

command to build docker image -> docker build -t slot-validation:v0 .

command to run docker container -> docker run -p 8000:8000 slot-validation:v0 
