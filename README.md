## Insight Coding Challenge- Consumer Complaints

### Problem
Given a government-collected file of consumers complaints against companies regarding different financial products, calculate the number of complaints filed and how they're spread across different companies. 

The resulting report would indicate, for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

### Main files
- `complaints.csv`  input file
- `report.csv`  output file
- `count_complaints.py`  my source code 
- `run.sh`  shell script to run the source code with input/output file arguments

### Approach

I tackle the task by 

1. Sort through the financial products to produce a list of unique products;
2. For each product, sort through the years to find for each year, the respective number of complaints against each company;
3. If for a product there is no data for a certain year, then that year is skipped;
4. Count the total number of complaints, the number of different companies against which these complaints are, 
   and the highest number of complaints against one particular company.
5. Produce the report file with each line documenting the product, the year, the total number of complaints, 
   the number of companies involved, and the percentage of the highest number of complaints against one company among all complaints,
   by dividing the highest number by the total number of complaints.
   
I choose to use `namedtuple` for the data structure. From the original `complaints.csv` file, I keep only the relevant columns of 
`Date received` (from which I parse out the year), `Product`, and `Company`.

For the calculation, I use `Counter` to find unique occurences of products and of years, and then loop through product and year
to count the number of companies and the respective number of complaints.
   


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


