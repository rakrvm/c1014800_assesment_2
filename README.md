#C1014800_Assesment_2

## Overview:
This program is used to store a set of data to a text file. It utilises user input to write to the file. When the program is ran
it gives the user 3 options, to write to the file, to search through the file, to edit text in the file. This is a simple program to use
but gives access to all the neccessary features that the user may need. The data is stored in a simple text file that is connected 
to the code. 

## Assumptions:
The assumptions I have made for this program are;
- The user will use correct formats and follow the formats. There is a lack of error checking within the program so I have assumed 
that the user will input full names and when putting in things such as dates they will use DD/MM/YY.
- Another assumption I have made for the program is that the user will want to end the program once finished with it all.
- Another assumption I have made is that when they are editing something they are only editing that specific thing, for example
editing names if they put in "John"" and want to edit "John Doe" they will only edit "John" out of "John Doe". So if they
edit it and replace "John" with "Ben" it will change to "Ben Doe".
- Another assumption I have made is that when searching for something in the code and they search for "John" and the contacts
name is "John Doe" it will not show "John Doe". In order for them to search they need to ensure to search full names. 
- If you want to search through the whole file you will need to type "Name" and it will print the whole file. 

## How to use:
The program is very simple to use. It is a matter of answering all the necessary questions that get printed in the terminal;
- Start the program normally.
- Use "Y" or "N" to answer the questions when they pop up. For example when you start the program it will ask if you want to 
add a contact and then you input "Y" and will take you through the process of adding a contact. If you want to edit a contact
you will need to go through and type "N" on adding and editing first and then it will bring up the option to edit a contact. 
- If you want to do something from the previous question you will need to end the program and go from the start. For example 
if you want to add a contact but your on the section to edit a contact you will need to restart the program in order to do this.
- The program will end when you type "N" on all of the questions.

## Use Case:
The program asks the user what they would like to do. For example for adding a contact the program will;
- Ask the user "Do you want to add a contact? (Y/N): " and the user will respond by typing "Y".
- The program then asks the user one piece of information at a time e.g "Full Name:", "Address:" and so on. 
- The user will follow by adding the data piece by piece e.g "Full Name: " they input "John Doe".
- The program takes all these inputs that the user has put and copies them into a text file in a format of "Name: John Doe"
and so on. 
- They can then either choose to add more contacts by answering "Y" when the question comes back up or choose to move on.
