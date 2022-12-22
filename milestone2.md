<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 21/12/2022 19:40:26</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027225-2b019a48-999d-48ff-9e60-631165b0d3d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add item page with data filled in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027224-581c48d8-7047-4849-ab97-ae8dc70ab78b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Db table screenshot with the new item as the last entry<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The input is received as form data. In the backend, the data is<br>verified and then entered into the db by a simple insert statement.<div>In addition,<br>visibility is set as true if stock &gt;0</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/21">https://github.com/Adhithya7/IS601-007/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/admin/item">https://is601-ap2823-project-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027223-28b44a95-cfe7-4048-934f-33ecd2af5a74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product listing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027221-8c28ff01-eba1-437e-9fdb-806f33da8b99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product listing page with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027217-7a5f0674-91d3-49c1-8a06-dd1860c77b27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product listing page with sort filter applied on unit price<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027216-db3b488b-3855-43d4-aab2-58c300adca94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet for the product listing page (with filters and sorting logic)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>In the listing page, all products with visibility = True are fetched. On<br>top of this data, filters and order by is applied.<div>For Name and description,<br>like filters are used</div><div>For sorting, Order by command is used. User can specify<br>if the items should be sorted by asc or desc order.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/22">https://github.com/Adhithya7/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/shop">https://is601-ap2823-project-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027214-d931785b-af57-4f18-a036-f5f6aed7807e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin product listing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>In this page, all items are fetched from the products table regardless of<br>the visibility. ie.&nbsp; A simple select * command with a limit value and<br>no other filters<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/23">https://github.com/Adhithya7/IS601-007/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/admin/items">https://is601-ap2823-project-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027208-44ea1e2f-5be1-49bb-9c11-170e6627a1fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Public shop open page with edit option for admin user alone<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027206-1bfd6568-f7aa-4edc-a7ac-5efa29599efa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit option on product view page for admin user alone<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027205-80fc5ef1-6104-4360-a664-a1260a9caf3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin product listing page with edit option<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027206-1bfd6568-f7aa-4edc-a7ac-5efa29599efa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing: Name is football<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027203-3ce8d638-28a6-4ede-a847-5673c94c97e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful edit: Name is changed to soccer<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027198-9c32803e-b257-4657-961a-16b1b896ca3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Listing page after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>All edit buttons have the default action.&nbsp;<div>First the form is prefilled by querying<br>the db.</div><div>Next, if any attribute is changed, an update call is made in<br>the backend.</div><div>Also, for each update call, a check is made to see if<br>quantity is 0. If the quantity is 0, visibility is set as false<br>as well.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/23">https://github.com/Adhithya7/IS601-007/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/admin/item">https://is601-ap2823-project-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209029026-fd79407c-99b5-4df6-a99d-e7cb76e42181.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product listing page with view button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027197-f929b5dc-8c99-4b4e-b079-b2105772584d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>When a user clicks the view button, a call is made to shop_item<br>endpoint. In the backend, data of that particular items is fetched from db<br>and displayed in the frontend<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/24">https://github.com/Adhithya7/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/shop/item">https://is601-ap2823-project-prod.herokuapp.com/shop/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027196-6e38a2f8-00f2-4f93-ad8e-c65f1720344b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message: Successfully added to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027193-b8ee09e6-8d4f-474e-a789-b4e5d41da4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Non logged in users are unauthorized to add to cart or view cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209028027-7e1f4d96-d510-4b29-bac4-70bda1ca84bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart table with a few records<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>Each user can have only one cart at a time.<div>Once the order is<br>placed, the cart is cleared.</div><div>Also, users can edit the quantity of the items<br>in their cart at any time.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>When an user clicks on add to cart button, that particular item is<br>added to their cart.<div>In the backend, cart table has an item inserted for<br>that particular item. One user will have multiple entries in the cart table.<br>Each row in the table is associated to each item in their cart.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/25">https://github.com/Adhithya7/IS601-007/pull/25</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027189-0c4779f5-9aae-497b-8953-c18d567f7cf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart page with all the above requirements satisfied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>After the cart items are fetched from the db, the subtotal is calculated<br>in the frontend by multiplying the unit price with the quantity. This is<br>shown as subtotal<div>In the frontend, all the subtotal values are added and displayed<br>in the end as total. Namespaces are used in the frontend to ensure<br>that the scope of the <code>total</code> object is available till the end</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/25">https://github.com/Adhithya7/IS601-007/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/cart">https://is601-ap2823-project-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027188-88984dd1-3eaf-4fe7-815f-2e072ff8fbbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully updated quantity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027187-5951a32d-6ba2-494d-93a2-770c073713b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item gets deleted when quantity is 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027187-5951a32d-6ba2-494d-93a2-770c073713b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item gets deleted when quantity is less than 0 as well<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>When an user sets the quantity as 0 or a negative values, it<br>is considered as item deletion in the backend. i.e that particular item is<br>deleted from the cart of that particular user<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/25">https://github.com/Adhithya7/IS601-007/pull/25</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027185-b92d0c7e-6977-4cc8-b7c6-2bfc0c79cc1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Single entry deleted from cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/209027184-ac0a9977-a545-4171-aeb9-f6563ad23aaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All items deleted from cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>For each delete request, that particular item is deleted from the cart table.<br>ie. a delete command is issued where userid=current user and item_id= respective item<br>id.<div>While clearing a cart, all items associated with that particular user is deleted<br>from the cart table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/25">https://github.com/Adhithya7/IS601-007/pull/25</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Did not face any major issues in milestone1.<div>However, Trying to align the footer<br>and styles for the frontend was quite tedious. Solved this by adding custom<br>css templates in layout.html</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/login">https://is601-ap2823-project-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ap2823" target="_blank">Grading</a></td></tr></table>