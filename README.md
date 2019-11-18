# Apriori-Algorithm
Initially used for Market Basket Analysis to find how items purchased by customers are related

### Basket Data
1. Retail organizations, e.g., supermarkets, collect and store massive amounts sales data, called basket data.
2. A record consist of transaction date and items bought<br/>
<br/>Basket data may consist of items bought by a customer over a period.

### Example Association Rule
90% of transactions that purchase bread and butter also purchase milk
<br/>   Antecedent: bread and butter
<br/>   Consequent: milk
<br/>   Confidence factor: 90%
### Association Rule Definitions
1. A set of items is referred as an itemset.
2. A itemset that contains k items is a k-itemset.
3. The support s of an itemset X is the percentage of transactions in the transaction database T that contain X. 
4. The support of the rule 𝑋⇒𝑌 in the transaction database T is the support of the items set 𝑋⇒𝑌 in T.
5. The confidence of the rule 𝑋⇒𝑌 in the transaction database T is the ratio of the number of transactions in T that contain 𝑋⇒𝑌 to the number of transactions that contain X in T.

### Applications
1. Market Basket Analysis: given a database of customer transactions, where each transaction is a set of items the goal is to find groups of items which are frequently purchased together. 
2. Telecommunication (each customer is a transaction containing the set of phone calls)
3. Credit Cards/ Banking Services (each card/account is a transaction containing the set of customer’s payments)
4. Medical Treatments (each patient is represented as a transaction containing the ordered set of diseases)
5. Recommender system
