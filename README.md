## Insight Coding Challenge- Consumer Complaints

### Problem
Given a government-collected file of consumers complaints against companies regarding different financial products, calculate the number of complaints filed and how they're spread across different companies. 

The resulting report indicates, for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

### Main files
- `complaints.csv`  input file
- `report.csv`  output file
- `count_complaints.py`  source code 
- `run.sh`  shell script to run the source code with input/output arguments

### Approach

The task is divided into two parts. The first part is to create a data structure. The second part is the calculation.


### My Repo directory structure

    ├── README.md
    ├── run.sh
    ├── src
    │   └── count_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── test_1
        |   ├── input
        |   │   └── complaints.csv
        |   |__ output
        |   │   └── report.csv
        ├── my-own-test_1 (using a subset of the Insight-provided dataset)
        |   ├── input
        |   │   └── complaints.csv
        |   |── output
        |   |   └── report.csv
        ├── my-own-test_2 (using the full Insight-provided dataset)
            ├── input
            |   └── complaints.csv
            |── output
                └── report.csv


