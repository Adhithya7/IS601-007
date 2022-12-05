<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 04/12/2022 21:19:45</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529268-3b3e6dbf-2bd3-4e50-add7-bb90fd45b0e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page with correct UCID and section (Running on heroku dev)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529267-cf39a92c-de08-4e1d-b077-6d0eec10e54b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DBeaver screenshot with both the tables created (UCID is visible as well)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529266-a1981da6-91f1-4d7a-a2a1-0f0a66119c15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>import route with all the todo&#39;s addressed (Part 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529265-123d06d4-0977-4252-bbda-4a2e34570e4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>import route with all the todo&#39;s addressed (Part 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529261-f369dfd1-cdee-4e9a-80ab-6a69bfc2839e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Imported successfully and the counts are flashed as well<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529264-d680a3bb-4570-400a-95f1-c87c220cbaab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error thrown when the selected file is not a csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529263-0efce40d-e67a-47a8-ad43-dc3c9924b614.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error thrown when no file is selected<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529256-071e2119-d97a-403c-ad3e-f265ba1ae91d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Screenshot of employee table after import<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529259-dfc4952e-7efd-4f04-bbdd-3951a5894bb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Screenshot of companies table after import<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529255-9499ebe2-6442-46d3-bf67-0b67b4409590.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add employee route : All todo&#39;s are addressed, NOTE: Since wtforms are used,<br>validations are done on the html side itself, Thus I haven&#39;t added flash<br>messages for the wtform fields<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529253-f815aee9-c0da-4041-aa55-f77fcf3edd89.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529252-a7f6723d-a395-40b0-a8b0-71f903964559.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee added successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205534506-dab02726-6dd0-44d1-b37e-9ab6568ed725.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First_name missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205534505-6f1701c3-d933-4059-bbf0-86795cb30b3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last_name missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205534504-493d93f8-eb47-4d90-a7f2-457466f608ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205534502-6fa7819b-8f79-4f18-97a0-fa3e7216f153.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>wrong email syntax error (WTform error)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529245-2abb42dc-3989-456a-aa6a-d58e3738c806.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Db row of the newly inserted employee <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529244-665ace40-4124-4e5d-a84c-ada3188c1bce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Search Route: All todo&#39;s are addressed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529243-717ed1d1-a82f-48d0-8288-b4e9d6e4e931.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First_name filter is applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529241-2caea88a-31d1-434d-834d-1ec2c571d837.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name filter is applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529240-f54ebf03-26a8-47c6-9103-a0aa7614248b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email filter is applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529238-fe5ba689-40e0-4324-8662-51a8c0bf6177.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company filter is applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529236-dfad3fec-f555-4630-99a4-8e64cadafecd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asc filter is applied on last_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529237-6a62e306-2444-4beb-affc-7670cf84233b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>desc filter is applied on first_name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529234-3145f78f-dcee-4586-8976-a6b776408560.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee edit Route: All todo&#39;s are addressed NOTE: Since wtforms are used, validations<br>are done on the html side itself, Thus I haven&#39;t added flash messages<br>for the wtform fields<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529233-8558bf76-4627-4244-b7ab-69b5cff86fbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529232-bd0d41e9-b559-436b-bdba-e04c163e4b2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit - Last name has been updated from 123Test to<br>123Test_edited_now<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529231-e717d7d5-487d-4814-9fd4-b4506641444a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529230-44a7c97e-de1e-4e7f-9394-c192ef8b8f5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row after editing - Last name has been updated from 123Test to<br>123Test_edited_now<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529229-1aebf64a-57e3-49cc-b97a-76c6680a9172.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Add Route: All todo&#39;s are addressed NOTE: Since wtforms are used, validations<br>are done on the html side itself, Thus I haven&#39;t added flash messages<br>for the wtform fields<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205532106-b3082ddc-739b-480b-9b67-1a3977cbdcb4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205531924-5ee2ce78-ac95-45cf-8fc7-3ee2b4279783.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company added successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205532477-360f9753-fcba-44ba-9a70-08de286e474a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529440-e5503e59-a4de-4d87-9804-ca5cc04b7870.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/205532400-dda4c0f1-5f80-4c94-99b9-59732601f82c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529439-7673b924-8a01-4151-8e06-59bf51f40e69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip missing error (WTform error instead of flash message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529438-be55955a-5051-40f2-944d-249e49820e41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country and State missing error (Flash messages are shown in this case because<br>WTforms are not used for these two fields)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529437-74efae15-641c-4cad-ba99-678b00ac8c20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Row of newly inserted company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529434-d583fa71-eff1-4a23-8edd-83cfe64b3cc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Search route: All todos are addressed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529432-7179eaaf-ce6e-4738-95be-da67e24f621d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529431-02118cc5-36fb-4959-8344-29e5b9e01a1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529430-6f054849-e783-4077-ac32-8c8b29f39b04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529427-2fd73e79-89e8-49dd-8650-d3eb88414f97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with asc filter applied on city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529429-a5acec41-4b7e-4024-8819-3a95f6c1b8a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with desc filter applied on name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529425-0fff984d-9b65-4d19-8962-152aa4dc256b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company edit route with all the todo&#39;s addressed (Part 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529423-9ceed9ea-0944-40a6-bbc9-f02c855ebfd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company edit route with all the todo&#39;s addressed (Part 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529421-1cf86ae6-5506-4765-a7d1-3f0187253d62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529420-007183e1-d4f7-4dce-90cb-e4ddac76c61d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data after editing (city is changed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529422-b0bbb5f3-af28-4e23-bb91-ac89c1bacc82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529419-fcc6ac81-2c35-4c7d-8456-ad187a882697.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row after editing (city is changed from gotham to metropolis)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529418-da500ff7-fe73-47ec-a6c6-fe5d6bc7bf5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete employee route: All todos are addressed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529416-7697a9ac-de51-4a3b-afef-87244050c260.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529414-13335635-8e96-4e52-a624-3539579fc8f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529412-e93a2447-71cd-42f3-b9e8-193ed99d94df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete company route: All todos are addressed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529411-b30b8947-903b-48a6-9719-adccd90ba901.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529410-c15f96a5-a799-447f-b790-a31574aeca0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529409-02a353d0-8202-4154-9545-20c24c275e70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest results using VSCode extension<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113129053/205529408-7dadff4f-5dd7-47a2-83d4-79d884d6118f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest results using terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Faced a few issues while using wtforms instead of traditional forms:<div>1. Making a<br>post call to endpoints using wtforms did not update the form fields as<br>expected - Fixed it by passing request.form to the WTForm object</div><div>2. Validate_on_submit did<br>not work as expected for direct post calls (since there&#39;s no submit action<br>involved) - Removed server side WTForm valdation and added pythonic validation</div><div>3. Passing Column<br>and Order as args to select query did not yield the expected result<br>- Fixed it by embedding Column and order in the select query rather<br>than passing them as args</div><div><br></div><div>Apart from this, learned how to incorporate jinja templates<br>and jinja expressions.&nbsp;</div><div>In addition, gained a practical understanding of html and bootstrap elements<br>(had a vague understanding based on class slides before working on the project)</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ap2823" target="_blank">Grading</a></td></tr></table>