# Assignment 2 - Probability & Statistics

## About the Project
This is my solution for Assignment 2.
The assignment focuses on two main topics:
1.  **Probability:** Calculating sample spaces and specific probabilities from scratch.
2.  **Statistics:** Analyzing a dataset (`iris.csv`) to calculate Mean and Standard Deviation.

**Constraint:**
As required, I did not use built-in functions for calculating probabilities or advanced statistical libraries. [cite_start]I implemented the logic using loops, conditions, and mathematical formulas[cite: 272].

## The Tasks

### Question 1: Children Sample Space
* **File:** `[YourID]_1.py`
* [cite_start]**Goal:** Receive the number of children in a family, generate all possible gender combinations (Boy/Girl), and calculate the probability of having **exactly two girls** [cite: 275-276].
* **How it works (My Implementation):**
    * I calculate the total number of options ($2^n$).
    * I use a loop to iterate through all options. Inside the loop, I use logical operations (modulo `2`) to determine the "Boy" or "Girl" sequence for each family (similar to binary counting).
    * I verify the length of each family using a `while` loop to ensure correct padding.
    * Finally, I iterate through the generated `final_families` list to count how many tuples contain exactly 'Girl' twice, and divide by the total options to get the probability.
* [cite_start]**Input Handling:** The code includes `try-except` blocks to handle non-integer inputs or negative numbers.

### Question 2: Iris Dataset Statistics
* **File:** `[YourID]_2.py`
* [cite_start]**Goal:** Analyze the `iris.csv` file containing flower dimensions (Sepal Length, Sepal Width, Petal Length, Petal Width)[cite: 280].
* **Calculations:**
    1.  [cite_start]**Mean (Average):** I sum up all values for each column and divide by the number of rows[cite: 282].
    2.  [cite_start]**Standard Deviation:** I calculate the variance (distance of each point from the mean) and then the square root to find the standard deviation for each of the 4 dimensions[cite: 284].

## How to Run
1.  Make sure you have Python installed.
2.  Ensure `iris.csv` is in the same folder as `Question2.py`.
3.  Run the files via terminal:
    ```bash
    python [YourID]_1.py
    python [YourID]_2.py
    ```

## Example Output (Q1)
Input: `4`
Output:
* A list of 16 tuples: `[('Boy', 'Boy', 'Boy', 'Boy'), ...]`
* [cite_start]Probability: `0.375` (which is 6/16)[cite: 278].
