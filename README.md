#  Hadoop-MapReduce-Python

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Hadoop_logo.svg/1000px-Hadoop_logo.svg.png)](https://nodesource.com/products/nsolid)

#### Description
  suppose we have the following two datasets :
 - Users (id, email, language, location)
 - Transactions (transaction-id, product-id, user-id, purchase-amount, item-description)
  ##### Example
Users (id, email, language, location)
| user_id       | email       | language  | location |
| ------------- |:-------------:| :-----:| :------------:|
| 1001 | A@gmail.com | English | Germany |
| 1002  | B@gmail.com | Arabic   | Egypt |
| 1003 |  C@yahoo.com | French |Canada |
| 1004 | D@fcih.edu.eg    |Englsih | Egypt|

Transactions (transaction-id, product-id, user-id, purchase-amount,item-description)

| t_id       | prod_id | user_id  | pru_amount | item_desc|
| ------------- |:-------------:| -----:|------------:|-----------:|
| 1001  | 5 | 1003 | 500| Description |
| 1002  | 6 | 1004   | 700| Description |
| 1003 |  9 | 1004 |400 | Description |
| 1004 | 2 | 1001 | 100| Description |
### Aim
  is to find the number of unique locations in which each product has been sold.
  to do that we need to join the two datasets and start to extract informations.
  - create a new data set that contains only three columns
   (user_id,prod_id,location) but __How?__
  here we will start our fist __JOB__ which is responsible for mapping the two tables to the following style
####  Merging:
| user_id       | prod_id       | location  |
| ------- |:------:| -----:|
| 1001 | - | Germany |
| 1001 | 5 |   - |
| 1002 | - |    Egypt |
| 1002 | 6 |    - |
| 1003 | - |    Canada |
| 1003 | 2 |    - |
| 1001 | - |    Egypt |
| 1001 | 2 |    - |

and then reducing it to get each prod_id wiht it's location as following
### Reducing:
| prod_id       | location       |
| ------------- |:-------------:|
| 5    | Germany |
| 6      | Egypt      |
| 2 | Canada      |
| 2 | Egypt      |

Now we had finished __JOB ONE__ what is remains?
we will start the __SECOND JOB__ to start counting each location a product has purshuaces in. And her the mapper is doing nothing except getting data and pass it to the reducer. And then the reducer should start counting to get the following resutl.
### Running second Job:
| prod_id       | no of locations       |
| ------------- |:-------------:|
| 5    | 1 |
| 6      | 1      |
| 2 | 2      |


####system requirments:
 * Python 2.7
 * Hadoop 2.8.1