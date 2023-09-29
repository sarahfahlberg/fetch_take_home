# Fetch Take-Home Test
## Sarah Fahlberg

Please use the instructions below to setup and run the health check program:
1. [Download conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if not already installed. Or if you already have conda, consider running:
```bash
conda update -n base -c defaults conda
```
2. Install dependencies
```bash
conda env create -f env.yml
conda activate health-check
```
Ensure that `(health-check)` appears before your line in terminal
3. Run html_health_check.py with the input argument. 

Example:
```bash
python html_health_check.py sample.yml
```
