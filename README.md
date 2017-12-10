#  Hadoop-MapReduce-Python

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Hadoop_logo.svg/1000px-Hadoop_logo.svg.png)](https://nodesource.com/products/nsolid)

#### description
  suppose we have the following two datasets :
 - Users (id, email, language, location)
 - Transactions (transaction-id, product-id, user-id, purchase-amount, item-description)
  ##### Example
- Users (id, email, language, location)
 > id&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;language&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location
 > 1001&nbsp;&nbsp;&nbsp;&nbsp;A@yahoo.com&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;English&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Germany
 > 1002&nbsp;&nbsp;&nbsp;&nbsp;B@gmail.com&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arabic&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Egypt
 > 1003&nbsp;&nbsp;&nbsp;&nbsp;C@fcih.edu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;French&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Canada
 > 1004&nbsp;&nbsp;&nbsp;&nbsp;D@gmail.com&nbsp;&nbsp;&nbsp;&nbsp;English&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Egypt
- Transactions (transaction-id, product-id, user-id, purchase-amount,item-description)
> t_id&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prod_id&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User_id&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pur_amount&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item_desc
> 1001&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1003&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description
> 1002&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1004&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description
> 1003&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1004&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description
> 1004&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1001&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description

### Aim
  is to find the number of unique locations in which each product has been sold.
  to do that we need to join the two datasets and start to extract informations.
  - create a new data set that contains only three columns
   (user_id,prod_id,location) but __How?__
  here we will start our fist __JOB__ which is responsible for mapping the two tables to the following style
####  After merging:
| user_id       | prod_id       | location  |
| ------------- |:-------------:| -----:|
| 1001    | - | Germany |
| 1001      | 5      |   - |
| 1002 | _      |    Egypt |
| 1002 | 6      |    - |
| 1003 | _      |    Canada |
| 1003 | 2      |    - |
| 1001 | _      |    Egypt |
| 1001 | 2     |    - |
and then reducing it to get each prod_id wiht it's location as following
### after reducing:
| prod_id       | location       |
| ------------- |:-------------:|
| 5    | Germany |
| 6      | Egypt      |
| 2 | Canada      |
| 2 | Egypt      |

Now we had finished __JOB ONE__ what is remains?
we will start the __SECOND JOB__ to start counting each location a product has purshuaces in. And her the mapper is doing nothing except getting data and pass it to the reducer. And then the reducer should start counting to get the following resutl.
### After second Job:
| prod_id       | no of locations       |
| ------------- |:-------------:|
| 5    | 1 |
| 6      | 1      |
| 2 | 2      |

# Implemntation
 to be continued
