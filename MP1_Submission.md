<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 23/10/2022 17:41:25</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197415740-1da5e74d-cb5b-4416-bafa-0025dad536d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the updated method to calculate cost and also the input<br>message displays the value in the currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419506-dfbc37d9-f36b-49fc-a0d4-667419493488.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows that calculated value returned from the function is being used.<br>It also shows how currency formatting is handled.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>The calculate cost function iterates over the objects in the <code>inprogress_icecream</code> list<br>and sums up the cost of each element in the list. In the<br>end, it is rounded off to 2 decimal points in order to handle<br>floating point precision.<div>2. Currency formatting is handled by using string formatting. ie. :.2f<br>in order to ensure that ##.## format is used at all times.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197417234-ab24392f-9c31-496e-8180-1bbbcfc9be74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception Handling: OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197417235-d9a00522-683e-45e1-8992-334a1696126a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception Handling: NeedsCleaningException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197417236-1b24a41a-d9b8-42d0-9961-dd9b94a05d52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception Handling: InvalidChoiceExceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197417237-7d1dd0af-1bec-40a5-8300-78e933e2913c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception Handling: ExceededRemainingChoicesExceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197417238-a8de7d96-260f-4793-ab37-19c62bba1527.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception Handling: InvalidPaymentException<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div><font size="2">Note: All the exceptions are handled by using recursion</font></div><font size="2">OutOfStockException:&nbsp;If any of<br>the item is out of stock, the user is prompted with a message<br>to choose a different item</font><div><font size="2">NeedsCleaningException:&nbsp;The user is prompted with a message to<br>clean the machine. If yes, the machine is cleaned and the user can<br>resume<br></font></div><div><font size="2">InvalidChoiceException:&nbsp;If the entered choice is an invalid choice, the user is prompted<br>with a message to choose again.<br></font></div><div><font size="2">ExceededRemainingChoicesExceptions:&nbsp;If maximum number of choices are exceeded<br>for flavors, the stage is automatically changed to toppings; If maximum number of<br>choices are exceeded for toppings, the stage is automatically changed to pay;&nbsp;<br></font></div><div><font size="2">InvalidPaymentException:&nbsp;If<br>the entered amount doesn't match the total, the user is prompted with a<br>message to try again.</font><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418464-d1839df2-1121-40f1-8ed7-9b680087a7bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 1 - container must be the first selection <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418465-e5f7b53a-5576-42a2-901b-70098e0919a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 - can only add flavors if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418467-ea47b898-754e-43b7-8978-bd888218cd54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 3 - can only add toppings if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418469-eea0d779-0891-4ed4-b425-4d1066a83bdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 - Can add up to 3 flavors/scoops<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418471-d670318b-de0e-4c6c-8ad9-136c3e72b622.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 - Can add up to 3 toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418472-0a77d1f8-18dc-4ffe-bd91-fe3e593ec81d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 - cost must be calculated properly based on the choices <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418462-d8558383-3f9d-4348-bc0b-3b4c69d7ee2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Fixtures for three different sales<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418562-5838e623-fc38-45f9-9557-b80f5ea19161.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 - Total Sales (sum of costs) must be calculated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418563-f29049ae-6305-48bb-8490-180b6600e8a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 - Total icecreams should properly increment for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197418561-1e512428-2ade-4a62-a91c-63c40dd40407.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All tests passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test1:&nbsp;Checks if an exception is raised when a flavor/topping is picked before&nbsp;a container<br>is picked.<div>Test2:&nbsp;Checks if an exception is raised when an out of stock flavor<br>is chosen</div><div>Test3:&nbsp;Checks if an exception is raised when an out of stock topping<br>is chosen</div><div>Test4:&nbsp;Checks if an exception is raised when more that 3 scoops are<br>picked</div><div>Test5:&nbsp;Checks if an exception is raised when more that 3 toppings are picked</div><div>Test6:&nbsp;Checks<br>if the cost returned by the calculate_cost method is correct by comparing with<br>manually calculated cost;&nbsp;This check is tested for 4 different combinations of cup,flavor and<br>topping</div><div>Fixtures are used for tests 7 and 8. Three different sales are simulated<br>and total_sum and total_icecream is evaluated against this fixture object</div><div>Test7:&nbsp;Checks if total_sales is<br>calculated properly. This is done by comparing manually caluclated cost with the object<br>returned by the fixtures</div><div>Test8: Checks if total_icecream is incremented properly. This is done<br>by check if the count matches with the total number of simulated sales.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/5">https://github.com/Adhithya7/IS601-007/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Learned how to play around with test cases.<div>2. Learned about fixtures.</div><div>3. Faced<br>issues while tracking the state of the objects returned by fixtures. Had to<br>test out a bit to understand how it works internally.</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419369-7caae0ed-77ce-47af-b852-ba614aa29c47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419370-1c9b6640-3ac1-4f65-a773-0af3c7ef8936.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution and invalid choice exception handling<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419371-a337fef6-f13e-43e8-9d38-51a0ea22680c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution and max scoops exception handling<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419372-5b211481-a238-4cc2-b39b-15eda0eef2e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution and no flavor/topping chosen exception handling<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/197419373-b6441d7e-c47e-4869-868f-2b952e5255b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Succesful execution and invalid payment exception handling<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ap2823" target="_blank">Grading</a></td></tr></table>