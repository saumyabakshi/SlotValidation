# SlotValidation

Assumptions : 

1.For finite entity post api, I have handled the case when support_multiple and pick_first have either (true, false) or (false,true) . For the cases (true, true) and (false,false) I've assumed the default values as mentioned in the function and treated them as (true, false)

2.I have allowed duplicate slot values to be processed.

3. For the numeric entity post api, I've assumed same as above, default values (true, false) for the (true,true) and (false,false) case. In case of no constraint and no value , Ive returned the response as expected by 'no value' condition.

Docker:

command to build docker image -> docker build -t slot-validation:v0 .
command to run docker container -> docker run -p 8000:8000 slot-validation:v0 
