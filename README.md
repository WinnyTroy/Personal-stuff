# Personal-stuff

  
troy is the basic setup of a blogging site. It has been structured using HTML/CSS.  It also uses Bootsrap for front-end styling.

# Nifi Account Details Flow
------------------------------------------------------------------------
This flow enables us fetch details for various accounts(Private and Organiational).
It takes either the email or the account username as input. The verification on which of the attribute to use to begin the flow is done automatically in Nifi by running the input through a regular expression that checks if the input is an email or not.
If an email is provided, Nifi uses this to make a `GET` call to Ona's user's endpoint to retrieve the username which is then used to obtain further account details.

**Nifi Account Details Data flow**
------------------------------------------------------------------------
- A `GET` call is made to the `profiles` endpoint. The response is a big payload of al the account details pertaining that account. More details about the account such as the account_type, account_plan and account_status are also received if the user has sufficient priviledges.
- These details are evaluated differently, dependent on whether the account is a personal or an organizational account. This happens since different details are received from different endpoints, thus they need to be routed to 2 different paths to make the appropriate calls.
- They are then inserted into the postgres database.



# Nifi projects and Forms flow
------------------------------------------------------------------------
- This flow provides us with the necessary details pertaining individual projects and forms associated with the username.
- It takes the username as input and uses this to make a `GET` call to the projects endpoint. This then returns the project details required.


**Nifi Projects Details Data flow**
------------------------------------------------------------------------
- A `GET` call is made to the `projects` endpoint.
- The response received is a payload detailing all the users and forms associated with the project in question. These users and forms are then extracted further using the Jolt Transform processor that applies a list of Jolt specifications to the flowfile JSON payload. The resultant would then be a list of all the users and forms associated with the same project whose details are also extracted.
- All details collected throughout the flow are then inserted into the database.

**Nifi Form Details Data flow**
------------------------------------------------------------------------
- This appears similar to the projects flow.
- A `GET` call is made to the `forms` endpoint.
- The response received is a payload detailing all the users and dataviews(filtered datasets) associated with the form in question. These users and dataviews are then extracted further using the Jolt Transform processor that applies a list of Jolt specifications to the flowfile JSON payload. The resultant would then be a list of all the users and dataviews associated with the same form whose details are also extracted.
- All details collected throughout the flow are then inserted into the database.


# Nifi counts flow
------------------------------------------------------------------------

The flow has been split into 3 main segments that fulfill different objectives.
    1. This first segment hits the users endpoint, with the need to obtain an array of all the users currently on the Ona platform.
        These users are then evaluated one at a time, retrieving the username for each indivual user that is then fed into the counts process group
    2. This second segment is the counts process group that obtains an aggregated value for private and public projects distinctly. Within the same process group we are able to obtain a count for all the projects created within the current month. This count data is then fed into the third segment
    3. The final segment stores the data within the counts model.

**Nifi counts Data Flow**
------------------------------------------------------------------------

- A `GET` request is made to the `users` endpoint. The response is a big payload of all the users currently registered on the ona platform.
- This response is then broken down into smaller payloads for each individual user, and evaluated to obtain the username for the user in question.
- With this username, another `GET` call is made to the `projects` endpoint i.e.``` https://api.ona.io/api/v1/projects?owner=${username} ```
This is done in order to recieve all the projects owned by that particular user.
- The response is then evaluated to once more. Within the payload, we check to evaluate if the `public` attribute is set to true or false. This is then what splits the flow into two separate flows according the value obtained from the public attribute. The flow is then routed to either public or projects.
- The UpdateCounter processor from Nifi is used to obtain the count value of both the public and private projects. The resultant value is stored within Nifi's Counter section at the menu at the very top right.
- After count information for the projects has been reveived, then the flowfiles are then merged back into one flowfile and another `GET` call is made to Nifi's counters API to obtain all the count values.
- Nifi replicates this count information to two variables i.e. the `All UpdateCounter's` and `UpdateCounters` variable. The two are more or less identical, except for the id's which are unique and the naming of the variabes. The count information though are more or less updated together simultaneously.
- The response is then transformed using the Jolt Transform processor to return only the valueCount received from the `All UpdateCounter's` variable gotten after hitting the Nifi counts API. All others are removed from the output reveived from this processor.
- The count data is then evaluated from the response and inserted into the Counts table

**Getting Project count for the current month**
------------------------------------------------------------------------
- This is obtained using Nifi's Expression Language.
- The date created attribute is evaluated from the response received after we hit the projects endpoint.
- This attributed is then equated to the current month and year. These two variables are as well obtained using Nifi's expression language. If the variables are a match then the project is counted, else it is not included in the count.

**Nifi counts Data Flow(with specified time period)**
------------------------------------------------------------------------
[TO BE UPDATED AFTER REVIEW IS DONE ON THE CURRENT IMPLEMENTATION. INCASE OF ANY CHANGE IN THE CURRENT FLOW]

**Notes**
------------------------------------------------------------------------

Nifi counters just values that you can increase or decrease given a particular delta. They are available to users from the menu located at the very top right: 

![screenshot_from_2019-01-30_12-42-42](https://user-images.githubusercontent.com/11174326/51984181-c5ea8780-24ab-11e9-8a58-949c9b7a526e.png)


They are quite useful if you need to monitor particular values all through your flow. 

you can notice that it’s possible to reset a counter to 0 from the counters table with the button in the last column (assuming you have write access to the counters based on the defined policies). This can be useful when doing some tests. At the moment however, Nifi does not provide a way to delete a counter, only reset. There was no delete option because if you deleted the counter, it would be recreated immediately if the processor was still running. Moreover, when Nifi is restarted, the counters are cleared completely.

The counters also can be reset programmatically by hitting the following endpoint:
           
           ```
           https://nifi.ona.io/nifi-api/counters/<counterID>
           ```
           

The count information can be obtained by hitting this endpoint: 
            ```
            https://nifi.ona.io/nifi-api/counters
            ```
