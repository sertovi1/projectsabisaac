# projectsabisaac
#Sabi Ertovi Isaac Btesh

# Final Project Proposal

## The Big Idea: What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.
+ We're building a tool designed for venture capitalists. It uses the Crunchbase API to send custom alerts (email, slack, telegram, google spreadsheets) and to analyze how different industries have been doing over the past years. This tool will help venture capitalists get information in an automated way on new investment opportunities and understand how the market is changing, all based on specific criteria they select (country, industry, investment size, etc…)

## Learning Objectives: Since this is a team project, you may want to articulate both shared and individual learning goals.

**Isaac’s Goals:** Learning how to use the CrunchBase API and master this API to then maybe learn how to use the PitchBook API which is a similar company that Crunch Base, since I work in Venture Capital, this can be a tool that my company can essentially use internally and if it’s valuable enough I can potentially sell the technology to other VC firms.
**Sabi Goals:** Learning how to use automated notifications using python and different packages. Exploring different kinds of packages available in python libraries and also internet.
**Mutual Goals:** Learning how to collaborate, work in a team on a coding project and learn discipline/trial and error by sticking to our project timeline.

## Implementation Plan: This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.
Crunchbase API (Documentation [Here] (https://data.crunchbase.com/docs/crunchbase-basic-using-api))
Library to analyze the trends and data
We are considering using Flask as an interface and HTML to allow user input, but this may vary depending on our progress and priorities.
Library to connect one of the desired channels to receive the information. (We will play around with different ones and then choose the best one/s)
Slack (More [here] (https://slack.dev/python-slack-sdk/))
For telegram, there is a Python telegram bot (More [here] (https://github.com/python-telegram-bot/python-telegram-bot))
Gmail API (More [here] (https://thepythoncode.com/article/use-gmail-api-in-python))
Spreadsheets (More [here] (https://developers.google.com/sheets/api/quickstart/python))


## Project Schedule: You have 6 weeks (roughly) to finish the project. Draft a general timeline for your project. Depending on your project, you might be able to provide a detailed schedule or only an overview. Preparation of a longer project is also accompanied by present uncertainty, and this schedule will likely require revisions as the project progresses.

The project presentation is due 12/04 and code submission is 12/09/
**Timeline:**
**Week 1 (Nov 13th-19th)**
Read and understand the CrunchBase API documentation
Set up initial environment and API keys.
**Week 2 (Nov 20th - 26th)**
Begin developing the core functionality for fetching and processing data from the Crunchbase API.
Write functions to test API connectivity.
Start playing around with Python libraries for data analysis.
**Week 3 (Nov 27th - Dec 3)**
Integrate the chosen type of notification API (telegram, slack, sheets, Gmail, we will choose one)
Finalize notifications and data analysis for industry trends
Conduct in-depth testing of our tool to ensure functionality and reliability.
Finish the README.
Find the best ways to showcase the results


## Collaboration Plan: How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.
+ We believe that separating tasks is not efficient because we both want to learn and understand every component of the code. This is why we decided that every time we work on the project, we will do it together by meeting in person. For small things that are not as important, we can divide tasks, such as writing the README. We decided that our method of communication is going to be WhatsApp for chatting and Slack for sending code to each other because it’s easier to view.  We will schedule 2-3 meetings per week, just in case we don't meet in person, we will have the meeting through Zoom. If the project is taking us longer than expected or we can’t meet in person, we might consider dividing tasks, but this is not the initial plan.


## Risks and Limitations: What do you believe is the most significant threat to this project's success?
+ I think that the thanksgiving break is the biggest threat to the success of this project, in the past thanksgivings we both tended to disconnect from school work, but in this case, we have no choice. Another reason is our busy schedules and other final projects for other classes. Isaac is also working part-time which can maybe cause issues in staying true to meeting times. But we are passionate about this project, so we will put in all the required time.

## Additional Course Content: What topics do you believe will be beneficial to your project?
+ API Integrations
+ Importing libraries
+ Flask
+ Html
+ Analyzing data 
+ Debugging





