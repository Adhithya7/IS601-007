<table><tr><td> <em>Assignment: </em> Sample Flask App and Readings</td></tr>
<tr><td> <em>Student: </em> Athithiyan Packirisamy (ap2823)</td></tr>
<tr><td> <em>Generated: </em> 30/10/2022 22:32:00</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/sample-flask-app-and-readings/grade/ap2823" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>&nbsp;Follow the slides from class.&nbsp;</li><li>&nbsp;Get the sample app deployed to Heroku dev</li><li>&nbsp;Once finished with the slides create a pull request from the lesson branch to dev (don't close it yet)&nbsp;</li><li>&nbsp;Create an m6_submission.md file in the same directory as the flask sample app&nbsp;</li><li>&nbsp;Fill in the deliverables below&nbsp;</li><li>&nbsp;Generate the markdown and paste the content into the new md file&nbsp;</li><li>&nbsp;git add/commit/push&nbsp;</li><li>&nbsp;Complete the pull request&nbsp;</li><li>&nbsp;Create a pull request from dev to prod&nbsp;</li><li>&nbsp;Complete the merge&nbsp;</li><li>&nbsp;Locally checkout dev&nbsp;</li><li>&nbsp;git pull the latest dev changes&nbsp;</li><li>&nbsp;On GitHub navigate to the location of the m6_submission.md file from the prod branch&nbsp;</li><li>&nbsp;Grab that direct link and submit it to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Proof App has been deployed </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the output of the app (including the url) showing it's running from Heroku dev</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/198917305-47ec233a-2805-4300-85b8-911687f43f35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>App output on heroku dev<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38016187/198917304-7e9bc6f0-1391-42c4-afce-f02dd92d84ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>App output on heroku dev with name query parameter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a direct link to the app here (prod url)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ap2823-prod.herokuapp.com/">https://is601-ap2823-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a link to the pull request from Flask-Sample-HW to Dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Adhithya7/IS601-007/pull/7">https://github.com/Adhithya7/IS601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Did you have any issues during setup and if so how did you resolve them, otherwise what did you learn?</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Workflow failed due to pytest not being installed - Checked the workflow<br>logs to figure this out and added it to the requirements file.<div>2. Heroku<br>app deployment failed - Checked heroku logs to figure out that gunicorn is<br>missing. Added it to the requirements file to resolve this error.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Readings </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> What can you tell me about docker? Describe the various steps needed to get an app ran inside a docker container in your own words</td></tr>
<tr><td> <em>Response:</em> <p>Docker is a virtualisation tool which enables developers to isolate and manage/deploy/test different<br>applications independently.<div>To run an app inside a docker, the first step is listing<br>out the requirements. Next, a dockerfile has to be written for the app,<br>and this file should contain the list of instructions which will run the<br>application. Each dockerfile runs on a particular base image. We can specify images<br>from local system, private repositories or docker hub. Using this dockerfile, new images<br>are built using the docker build command. These images can be run as<br>docker containers anywhere without any dependacy issues.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> What is Heroku? Why do you feel it was chosen for this class?</td></tr>
<tr><td> <em>Response:</em> <p>Heroku is a cloud application platform which is used for deploying applications on<br>a cloud network and can be accessed from anywhere. There are so many<br>other PaaS platforms available as well, such as AWS, Azure, GCP. I feel<br>Heroku was chosen for this class since it has student tier benefits and<br>also easy integration with github workflow. We are using heroku as the platform<br>for CI/CD workflows.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What is flask? List a few things you learned about it</td></tr>
<tr><td> <em>Response:</em> <p>Flask is a web framework on python which is used for developing web<br>applications. It has an inbuilt development server and allows templating using jinja2. This<br>feature is helpful in integrating frontend with backend.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> What is the difference between a Dockerfile and a Github Action .yml file?</td></tr>
<tr><td> <em>Response:</em> <p>A dockerfile is used for specifying the instructions to be run on top<br>of a base image. A docker image is built using this dockerfile. Whereas,<br>a github action yml file is used for setting up github workflow. A<br>github action file can be configured to watch a few branches and do<br>a set of instructions if at all any changes are made to those<br>branches. In our case, we&#39;ve used github actions to implement CI/CD by setting<br>up workflows and deploying the images on heroku.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/sample-flask-app-and-readings/grade/ap2823" target="_blank">Grading</a></td></tr></table>