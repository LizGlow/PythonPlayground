# Step-by-step to start analyzing data
### Project Scenarios
Suppose I were a teacher now and my goal is to identify which skills students excel in and which skills they struggled with over 3 months. In this project, We are going to work with **structured data**.

There are 4 main skills in my Korean class:
- Reading
- Listening
- Speaking
- Writing 

### Analytic Process
**1. Define Objective** <br />
Before you start, make sure to define what you want to achieve here. Read the [Project Scenarios](#Project-s-Scenarios)

**2. Data Collection & Gathering** <br />
There are several ways to collect data. We may collect data by conducting surveys, tests, quizzes, assignments, class activities, etc. However, We don't need to collect data here since we are going to work with the simulated data which is located in 👉 [simulated_dataset](https://github.com/LizGlow/PythonPlayground/blob/master/simulated_dataset/generated_students.csv)

**3. Import Data** <br />
We are going to use Pandas to import or load data
```
import pandas as pd
data = pd.read_csv(r'../simulated_dataset/generated_students.csv')
```

**4. Data Organization** <be />
In this part, we are going to use Numpy and Pandas 
```
data.head() #data inspection
data.info() #check data types and null
```
