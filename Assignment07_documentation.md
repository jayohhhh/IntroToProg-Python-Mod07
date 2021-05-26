__Jonathan Ou__  
__5/25/2021__  
__Foundations of Programming: Python__  
__Assignment 07__  

# Pickling and Exception Handling Documentation

## Introduction
In this week’s lesson, two power tools were explored in exception handling and pickling. Through exception handling, you can anticipate potential errors that users my commit on to the code and provide a detailed explanation on how to best troubleshoot as opposed to allow Python to provide its generic feedback. Pickling allows the user to store their data into binary form which may serve as simple protection and size saving. This is not an encryption technique and should not be employed as such.

## Exception Handling
Through web searching, the following website served as a good secondary source to the lecture as it provides a simple run through of utilizing exception handling as well as additional information that was useful in the script for this assignment.
https://realpython.com/python-exceptions/

## Pickling
Through web searching, the following website served as a good secondary source to the lecture as it gives a very simple explanation while going through the necessary inputs to utilize the pickle module:  
https://www.tutorialspoint.com/python-pickling  

## Exception Handling/Pickling Example
The following Figure 1 shows implementation of pickling and exception handling through my script. It starts by importing pickle which brings in the module. The start of the script beings with asking the user for inputs on lunch item and lunch time. Exception handling was employed to specify that the lunch item cannot have numbers in it. Through raising the exception in the code, I can choose a custom message to bring up to the user. It will be printed to the user to ensure that the next usage of the code will be successful. If the exception was raised through the use of else, the code will end right there and not allow the user to continue with the rest of the script. Successful input of the lunch item will allow the user to continue with the script and input a time. Next, these inputs are placed into a list which are then pickled into a dat file. The pickling process is similar to using write except the contents of the file will be stored in binary form. The script concludes by re-loading the pickled content and printing it back to the user. The user will see the unpickled content is indeed what they input at the beginning of the script.
![image](https://user-images.githubusercontent.com/29714047/119613518-03c4f580-bdb2-11eb-9758-cfe39748c438.png)

## Outputs
Figure 2 shows the output after committing the exception in the script. Inputting numbers will prompt the error and ends the script without any further prompts.
![image](https://user-images.githubusercontent.com/29714047/119613561-13443e80-bdb2-11eb-80af-09990de7c1f7.png)

Figure 3 shows the output of the script without exception, ending with the printed value of the unpickled lunch list.
![image](https://user-images.githubusercontent.com/29714047/119613582-193a1f80-bdb2-11eb-8f41-cb4b4c1cba10.png)

Figure 4 shows the output in CMD which mirrors the output shown in Pycharm. The contents are different due to the differing inputs but the output would be the same otherwise.
![image](https://user-images.githubusercontent.com/29714047/119613604-1fc89700-bdb2-11eb-9fa0-ed5330ec0f09.png)

The last figure, Figure 5, shows the pickled list in the LunchPlans DAT file. Here the contents are not simply the string that was constructed but a converted message. The contents were not hidden so this is not a method of encryption. 
![image](https://user-images.githubusercontent.com/29714047/119613630-26efa500-bdb2-11eb-871e-1bb67c427c9d.png)

## Summary
This week’s lesson sought to understand the concepts of pickling and exception handling. Through pickling, it is possible to store the information into binary form which can be stored until later use. Exception handling will prove to be a useful tool in the future as it will help future users identify trouble in code execution without consulting the creator through detailed explanations.

## Github Page
