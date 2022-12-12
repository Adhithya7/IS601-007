<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 12/12/2022 00:04:38</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961450-d2e41d24-cb22-4152-84c9-8fadbe34ae2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961449-c5bb7344-16ac-446e-b2f6-a73ef3799005.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961448-0725a2f1-459d-4be0-b74e-8ecf5065ce7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961446-6c0c2298-9c66-4f83-a323-8ab9a36f9b97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961447-b4377e1f-a9f7-4540-85d5-e5f5dc0bd3aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961453-0c084927-73de-4c3c-8a76-923a43412a4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Inserted data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961451-6bba50ef-fc73-40a7-9dec-e7fd5402fd22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful insert<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961445-81de6b1e-4c6b-4c2c-aad4-cff2fca78179.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User test1 is found in the table (id=6)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/11">https://github.com/Adhithya7/IS601-007/pull/11</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>WTforms are used for receiving form input and the form is validated<br>when it is submitted<div>2. WTforms have inbuilt validators. These validators show error messages<br>on the frontend before it makes a call to the backend. The unique<br>username, email validations are done in the backend by processing the error message<br>from the database. The database has constraints on the username and email.</div><div>3. Password<br>has a validator and before it is stored in the database, it is<br>encrypted using bcrypt. Bcrypt adds a salt value to the password and the<br>hash of this salt+password is stored in the database</div><div>4. Database is used for<br>storing the users information. Constraints are also added to the tables in the<br>database. Queries are made to the db using the db helper and the<br>response is served in the frontend</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961444-911b514d-2847-4f11-8d80-e4d1902158d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961443-84544534-9bf0-45a9-bd19-565130e5cd97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>non-existing user validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961442-7891e54f-be86-40e3-bceb-63d39921497b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/12">https://github.com/Adhithya7/IS601-007/pull/12</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>WTforms are used for receiving form input and the form is validated<br>when it is submitted<div>2. WTforms have inbuilt validators. These validators show error messages<br>on the frontend before it makes a call to the backend. The unique<br>username, email validations are done in the backend by processing the error message<br>from the database. The database has constraints on the username and email.</div><div>3. Password<br>has a validator and before it is stored in the database, it is<br>encrypted using bcrypt. Bcrypt adds a salt value to the password and the<br>hash of this salt+password is stored in the database</div><div>4. Database is used for<br>storing the users information. Constraints are also added to the tables in the<br>database. Queries are made to the db using the db helper and the<br>response is served in the frontend</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961441-4693075b-c167-4c39-8446-7266d419f8ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful log out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961439-5fdadbb5-47ae-493a-892a-e51f273235c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out user is not able to access login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/13">https://github.com/Adhithya7/IS601-007/pull/13</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Sessions are maintained using flask&#39;s inbuilt methods. Flask maintains the current session<br>by using flask_login. Current_user maintains the informatin of the current logged in user.<br>This value is used in the sessions across webpages to ensure that the<br>user remains logged in accross pages. We retrieve the current user_id and the<br>user_roles and maintain the same across pages&nbsp;<br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961439-5fdadbb5-47ae-493a-892a-e51f273235c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out user is not able to access login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961434-47321676-1496-4ed1-ad7b-28a6242a093c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User without proper role is not able to access role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961438-20e22f93-4b48-4a09-a545-06318ae64901.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with admin role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961436-c28af8a7-d425-4769-9c2d-add40f1c4003.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Userroles table with one assignment (for user admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961435-0db5b6e3-3fbc-4336-ae13-7ecfefec436e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>users in users table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/14">https://github.com/Adhithya7/IS601-007/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For login-protected pages we use the inbuilt decorator called login_required. This checks if<br>a user is authenticated or not<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For role-protected pages we fetch the roles attached to the session of the<br>user and see if it matches the desired roles. We use flask&#39;s inbuilt<br>permission requirement decorator to check the same<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961429-d0c81460-1878-4455-9a04-55fd9f47652a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed nav bar style<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961428-cdef4bbb-5d04-4593-818c-f55a2f471c35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed table style and rows are printed in a clean manner<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961427-ae69e03e-150f-4938-abb6-56eda309f59c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed form style<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/15">https://github.com/Adhithya7/IS601-007/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Changed the background color of navbar and form<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961439-5fdadbb5-47ae-493a-892a-e51f273235c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961434-47321676-1496-4ed1-ad7b-28a6242a093c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961430-a1af0584-9fd5-4e12-8bdb-d0c0d568ed0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page not found - Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961447-b4377e1f-a9f7-4540-85d5-e5f5dc0bd3aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/11">https://github.com/Adhithya7/IS601-007/pull/11</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>For webpages, we are overriding the default page for status codes 401, 404<br>and 403 by adding new templates.<div>For exceptions, we use regex match to see<br>if the message matches the desired regex format</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961427-ae69e03e-150f-4938-abb6-56eda309f59c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username are prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/16">https://github.com/Adhithya7/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The formdata is fetched in the beginning whenever a call is made to<br>thee endpoint. If the form values are present, they are fetched and displayed.<br>If not available, empty values are displayed<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961426-d627fc5b-79c1-4051-ab53-62019866d9ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961424-b168016b-5ea6-4126-9111-ca482a9ad47b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961423-314c8199-4d7a-4a5f-bf9b-08cc793bf05b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961422-775a28f8-0b0a-4cde-ad9d-95ab97128ea3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961421-9e587bc5-1581-40f4-aa02-6af9a0cae7bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Table before updating profile (for user admin- username is admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961419-fb518524-e12d-4f0b-a99a-e06de5f3520e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form with new value for username and profile is updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/206961418-f6d5b4c7-aa41-4e92-b619-f49666264291.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Table after updating profile (for user admin- username is changed to admin2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/16">https://github.com/Adhithya7/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>For email and username, update calls are made to the table by using<br>the user_id as the key. If the username or email already exists in<br>the table, the update query will fail because of the table constraints.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Faced issues while changing the css values and styles. Was unable to set<br>the desired css styles for forms. Later reverted to traditional hover style form<div>In<br>addition faced an issue while trying to incorporate login method. It was throwing<br>an error that current_user is unavailable. Later, I discovered that login manager was<br>not initialized in main.py</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-project-prod.herokuapp.com/login">https://is601-ap2823-project-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ap2823" target="_blank">Grading</a></td></tr></table>