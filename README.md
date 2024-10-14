## Supply Planning using Linear Programming with Python 🚛
*Where do you need to allocate your stock to meet customers demand and reduce your transportation costs?*


<p align="center">
  <img align="center" src="https://miro.medium.com/max/1280/1*y4AHwh75uQ771dEdO6sxJg.png">
</p>

Supply planning is the process of managing the inventory produced by manufacturing to fulfil the requirements created from the demand plan.

Your target is to balance supply and demand in a manner to ensure the best service level at the lowest cost.

### Article
In this [Article](https://towardsdatascience.com/supply-planning-using-linear-programming-with-python-bff2401bf270), we will present a simple methodology to use Integer Linear Programming to answer a complex Supply Planning Problem considering:
- Inbound Transportation Costs from the Plants to the Distribution Centers (DC) ($/Carton)
- Outbound Transportation Costs from the DCs to the final customer ($/Carton)
- Customer Demand (Carton)

### Problem Statement
As a Supply Planning manager of a mid-size manufacturing company, you received the feedback that the distribution costs are too high.
Based on the analysis of the Transportation Manager this is mainly due to the stock allocation rules.

In some cases, your customers are not shipped by the closest distribution centre, which impacts your freight costs.

### Your Distribution Network
- 2 plants producing products with infinite capacity
*Note: we’ll see later how we can improve this assumption easily*
- 2 distribution centres that receive finished goods from the two plants and deliver them to the final customers
*Note: we will consider that these warehouses operate X-Docking to avoid considering the concept of stock capacity in our model
200 stores (delivery points)*

### Question
Which Plant i and Distribution n should I chose to produce and deliver 100 units to Store p at the lowest cost?

## Code
This repository code you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain and Data Science consultant with international experience working on Logistics and Transportation operations. \
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://wwww.logi-green.com/). \

Please have a look at my personal blog: [Personal Website](https://samirsaci.com)
