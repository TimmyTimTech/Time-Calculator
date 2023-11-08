# Time-Calculator
The problem is with the condition that checks if the time is before 12 am. This condition will not be executed as the program has already determined that the total time is greater than 24 hours, and will proceed to convert the hours into pm format.

The corrected program should check if the total time is less than 12 am, and if it is, convert it into am format. If the total time is greater than or equal to 12 am, convert it into pm format.
In this code, I've removed the condition that checks if the total time is less than 12 am. Instead, I've added a condition that checks if the total time is less than 12 am, and if it is, it converts it into am format. If the total time is greater than or equal to 12 am, it converts it into pm format.


