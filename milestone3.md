<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 21/12/2022 20:20:35</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-shop-project/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209030684-0e078e83-dd25-4da6-b4ba-4ba4697210cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data for orders table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209030752-c311921c-1246-45da-8997-98172ad3b5e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data for orderitems table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032279-12a04925-f091-49f1-8a82-a366b1751bec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase UI is shown as pending order. User has to enter address and<br>payment details. Once done, they&#39;ll be asked to do the payment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032278-288406d3-baa9-42ff-9a40-c50276931639.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pending Purchase form with data filled. It has a link to go back<br>to cart as well. The items shown are non-editable as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032277-1c5c5fa1-be4d-4f13-988b-98488b2ec0b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here validation is done to check if address and payment details are supplied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032275-3bd35420-9e65-4c15-8c09-4e6892e83dc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here validation is done to check if paid amount matches the cart amount<br>and also if the stock and price of items are correct<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032274-5ba2ddaa-a979-4467-a3a5-ee3e17973770.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mock Payment done with wrong amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032273-9ff596f6-0597-47b1-9c6f-5abd69872e06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message thrown when money doesnt match the cart amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032271-df1fc952-d257-4a97-9e15-b000aabb7cd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Trying to update quantity of an item to 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032270-33ccd686-86a0-4e67-aef6-00ba827eb3b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error thrown while trying to update since the item doesnt have 8 available<br>units<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>When place order is clicked on cart page, the user will be<br>directed to place order page.<div>2. In this page, the cart details are verified<br>first. If the details are correct and the items are in stock, the<br>user is presented with a form to enter shipping address and payment details.</div><div>3.<br>Once done, the user will be redirected to make the payment.</div><div>4. If the<br>payment is succesful, the order will be confirmed. In the backend, the stock<br>and price is verified again. If the verification succeeds, an entry is made<br>into the orders table and for each item in the order, an entry<br>is made into the orderitems table.</div><div>5. If no issues pop up, those items<br>are removed from the cart table. In addition, the stock of those respective<br>products are updated as well.</div><div>6. The user is presented with a confirmation page<br>and the order id is also displayed.</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/27">https://github.com/Adhithya7/IS601-007/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/confirm_order">https://is601-ap2823-project-prod.herokuapp.com/confirm_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032269-de24cd2c-0076-48c3-be76-0d8bf63febdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order confirmation page with all requirement satisfied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>The address and payment information provided by the user is added to the<br>orders table when the order goes through. When the order is confirmed, these<br>details are fetched and rendered as a table.<div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/27">https://github.com/Adhithya7/IS601-007/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/place_order">https://is601-ap2823-project-prod.herokuapp.com/place_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032268-f3154f83-292d-4a3c-952f-a01e78e5167b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order listing page with view option for each order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032267-f1dd5e14-d830-4b79-a039-da875d5960af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All details of the order is shown in the view order page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>When an user tries to view all his orders, all the orders are<br>fetched from orders table with an user id filter.<div>Each item in the list<br>has a view option. When view option is clicked, data is fetched from<br>orders table and orderitems table by joining them on orderid and userid (inorder<br>to ensure that users cant see other users&#39; data).</div><div>After joining, the items ordered<br>in those particular order are retrieved and displayed as a table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/28">https://github.com/Adhithya7/IS601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/order?id=1">https://is601-ap2823-project-prod.herokuapp.com/order?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032265-4fe81989-dd0b-495c-8fe7-04cf17633e88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All orders are shown. View option is available for each order. In addition,<br>the username of the person who made the order is shown for each<br>order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032838-9d8c3190-c9c3-4be3-8628-326b52580cb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order details of a user that is not admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>Same logic is applied here as well. The main change here is the<br>initial query for fetching the order details.<div>The orders table is joined with the<br>users table in order to fetch the username.</div><div>Now, when view button is clicked,<br>the orders table is joined with orderitems table on itemid and the data<br>is fetched (user_id is not used since the user viewing the order is<br>admin)</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/28">https://github.com/Adhithya7/IS601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/admin/order?id=5">https://is601-ap2823-project-prod.herokuapp.com/admin/order?id=5</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209032993-f7f59f81-ce9f-435b-af60-567cf2cb9e8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart page with place order button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Faced a complex issue while trying to carry forward form data from the<br>pending purchase page to the confirmation page. Tried to fix this by relaying<br>the form elements from page to page. Faced a roadblock in this approach<br>since one of the pages worked on GET method.<div>Finally, fixed the issue by<br>using multiple redirects. (Since form data is not cleared when the request is<br>redirected)</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-shop-project/grade/ap2823" target="_blank">Grading</a></td></tr></table>