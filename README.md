# python_challenge
051223 Setting up this repository to complete this challenge; created folders PyBank and PyPoll
  
05/13 Was successful in pushing from Bash to GitHub.  GitHub does not like empty folders so was not able to add the "analysis" folders to the PyBank and PyPoll folders but will when it contains the applicable txt file. Worked around this by adding a .gitkeep file to each analysis folder, followed by git add, git commit, git pull, git pull.
Reference: https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/gitkeep-push-empty-folders-git-commit#:~:text=Git%20doesn't%20like%20empty,gitkeep%20file%20comes%20in.

5/13 Worked on penciling logic for PyPoll and figuring out how to count.  I also encountered an “I/O operation on closed file error” and read through several resources but none of them specifically helped me other than this one (https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file) which made me think about tabbing in correctly.  Correctly aligning commands eliminated that error.

5/14 Figured out how to count the lines in a csv via https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php
OK may have figured out the count and unique but need to check (11:45 am)
https://www.tutorialspoint.com/check-if-list-contains-all-unique-elements-in-python - got stuck
I think I need to do something like in list comprehensions (04)

5/14 Notes for PyBank
Adding elements in a list https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
Converting items in a list to values
https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
Getting max value info from Pan and discussion in studygroup (also included Raina, Eva, Hannah) and fixed with 
https://sparkbyexamples.com/python/get-index-of-max-of-list-in-python/#:~:text=Python%20Get%20Index%20of%20max,element%20and%20use%20the%20list.

5/17 PyPoll
Finally got my vote count per candidate. It was trial and error with how I was comparing variables in my lists and it turned out to be simple.  I had over complicated it and mixed values and strings and kept getting errors.
To make sure that I had the right vote total with a candidate I found the “extend” command to add two items to a list. https://sparkbyexamples.com/python/python-append-multiple-items-to-list/#:~:text=To%20append%20or%20add%20multiple,the%20end%20of%20the%20list.


5/15 Notes for PyBank
Finished PyBank.  Rounding help from: https://www.programiz.com/python-programming/methods/built-in/round
Got help from TA Andrew K. in figuring out how to call out the month by using the index position.
Printing to .txt file https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

5/16 PyPoll
OK after a lot of work looping through the candidate list I found this resource to id the unique candidates in the election data: https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python
Working through counting votes per candidate
