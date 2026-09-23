# Business Process Automation

A small Python automation project that simulates the processing of business requests from an Excel file.

The goal of this project is to automate a simple workflow: read incoming requests, validate the data, identify records that require manual review, and generate a separate Excel report.

## What it does

The script:

- Creates a sample Excel input file
- Reads and processes the input data
- Validates that request amounts are greater than zero
- Detects duplicate request IDs
- Identifies pending requests with an amount greater than or equal to 40,000
- Adds a reason explaining why each request requires review
- Generates a new Excel report containing the requests that require manual review
- Displays a processing summary in the terminal

## Technologies

- Python
- Pandas
- OpenPyXL
- Excel
- Git / GitHub

## Project structure

business-process-automation/
├── data/
│   ├── input.xlsx
│   └── review_required.xlsx
├── src/
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt

## Business rule

A request requires manual review when:

- `status` is `Pending`
- `amount` is greater than or equal to `40000`

The generated report also includes a `review_reason` column to make the result easier to understand.

## Data validation

Before processing the requests, the script checks for:

- Invalid amounts (`amount <= 0`)
- Duplicate `request_id` values

If invalid data is detected, processing stops before generating the final report.

## How to run

Install the dependencies:

```bash
pip install -r requirements.txt