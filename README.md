## Supply Planning using Linear Programming with Python 🚛
*Where do you need to allocate your stock to meet customers' demand and reduce your transportation costs?*

<p align="center">
  <a href="https://www.samirsaci.com/supply-planning-using-linear-programming-with-python/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/1280/1*y4AHwh75uQ771dEdO6sxJg.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>>

Supply planning is the process of managing the inventory produced by manufacturing to fulfil the requirements created from the demand plan.

Your goal is to balance supply and demand to ensure the best service level at the lowest cost.

### Article
In this [Article](https://www.samirsaci.com/supply-planning-using-linear-programming-with-python/), we will present a simple methodology to use Integer Linear Programming to answer a complex Supply Planning Problem, considering:
- Inbound Transportation Costs from the Plants to the Distribution Centres (DC) ($/Carton)
- Outbound Transportation Costs from the DCs to the final customer ($/Carton)
- Customer Demand (Carton)

### Problem Statement
As a Supply Planning manager at a mid-sized manufacturing company, you received feedback that distribution costs are too high.
Based on the Transportation Manager's analysis, this is primarily due to the stock allocation rules.

In some cases, your customers are not shipped by the closest distribution centre, which impacts your freight costs.

### Your Distribution Network
- 2 plants producing products with infinite capacity
*Note: we’ll see later how we can improve this assumption easily*
- 2 distribution centres that receive finished goods from the two plants and deliver them to the final customers
*Note: We will consider that these warehouses operate X-Docking to avoid considering the concept of stock capacity in our model
200 stores (delivery points)*

### Question
Which Plant i and Distribution n should I choose to produce and deliver 100 units to Store p at the lowest cost?

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Supply Planning Problem.ipynb` - Jupyter notebook with step-by-step analysis
- `supply_planning.py` - Standalone Python script
- `data/` - Folder containing input CSV files (df_demand.csv, df_inprice.csv, df_outprice.csv)

### Getting Started
```bash
pip install -r requirements.txt
python supply_planning.py
```

### Dependencies
- pandas
- pulp
- matplotlib
- seaborn


## Go further

- **The full write-up, with the reasoning behind the code:** [Supply Planning using Linear Programming with Python](https://www.samirsaci.com/supply-planning-using-linear-programming-with-python/?utm_source=github&utm_medium=readme&utm_campaign=supply-planning)
- **Test what you learned:** the [Supply Science App](https://supply-science.com/?utm_source=github&utm_medium=readme&utm_campaign=supply-planning) has the business optimisation quizzes, free and in the browser.
- **100+ case studies with their source code:** [samirsaci.com](https://www.samirsaci.com/?utm_source=github&utm_medium=readme&utm_campaign=supply-planning)

## About me

Samir Saci, supply chain engineer and data scientist with ten years in operations across Asia and Europe. Founder of [LogiGreen](https://www.logi-green.com/), creator of [Supply Science](https://www.youtube.com/@SupplyScience).
For consulting on analytics and sustainable supply chain transformation: [LogiGreen](https://www.logi-green.com/). More about me: [samirsaci.com/about](https://www.samirsaci.com/about/) · [LinkedIn](https://www.linkedin.com/in/samir-saci/)

