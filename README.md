# HR-Allocation-Application
Implementation of an optimal project staffing system. The system makes use of a decision-tree regressor to estimate the number of Human Resources(HR) per team.

Paper Link: - 


**Overview**

      The figure below depicts the working of the system.
<p align="center">
  <img src="https://github.com/AAnirudh07/HR-Allocation-Application/blob/main/assets/overall.JPG" />
</p>


**Dataset**

      A synthetically generated dataset was used to train the regression model. 
      It is available for download (in the documentation folder). 

**Front end**

      The front end takes the following information as input:
      1. Number of teams
      2. Number of engineers available
      3. Required engineer types and experience (per team)
      To run the front end:
           - install dependencies
           - execute 'npm start' from the front end folder


**Backend**

      The back end obtains an optimal project staffing by running the regression model. 
      It returns an excel file with the appropriate details to the front end. The file
      contents are visually represented as a pie-chart in the front end.
      To run the back end:
            - install requirements (pip install -r requirements.txt)
            - execute 'flask run' from the back end folder

**Tech Stack**

<p align="center">
      <img src="https://github.com/AAnirudh07/HR-Allocation-Application/blob/main/assets/frontend.JPG" />
</p>

**Tech Stack**
<p align="center">
      <a href="https://reactjs.org/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> 
    <a href="https://flask.palletsprojects.com/en/2.2.x/" target="_blank"> <img src="https://github.com/get-icon/geticon/blob/master/icons/flask.svg" alt="nodejs" width="40" height="40"/> </a>​

</p>
