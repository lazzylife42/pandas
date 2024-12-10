import pandas as pd

# ============================== Ex01 ============================== #
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | bigint  |
# +-------------+---------+
# name is the primary key (column with unique values) for this table.
# Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

 

# A country is big if:

#     it has an area of at least three million (i.e., 3000000 km2), or
#     it has a population of at least twenty-five million (i.e., 25000000).

# Write a solution to find the name, population, and area of the big countries.

# Return the result table in any order.

# The result format is in the following example.

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return big_countries[['name', 'population', 'area']]

# ============================== Ex02 ============================== #
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | low_fats    | enum    |
# | recyclable  | enum    |
# +-------------+---------+
# product_id is the primary key (column with unique values) for this table.
# low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

 

# Write a solution to find the ids of products that are both low fat and recyclable.

# Return the result table in any order.

# The result format is in the following example.

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    good_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return good_products[['product_id']]

# ============================== Ex03 ============================== #
# Table: Customers

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.

 

# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

 

# Write a solution to find all customers who never order anything.

# Return the result table in any order.

# The result format is in the following example.

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    customers_without_orders = merged[merged['customerId'].isna()]
    return customers_without_orders[['name']].rename(columns={'name': 'Customers'})
	
	# Création des DataFrames : Représenter les tables Customers et Orders en Pandas.
	# Jointure à gauche : Utiliser merge pour inclure tous les clients, même ceux sans commandes.
	# Filtrage : Trouver les lignes où customerId est NaN.
	# Nettoyage du résultat : Extraire les noms et renommer les colonnes.
    
	# pd.merge : Equivalent à une jointure SQL.
	# isna() : Détecter les valeurs manquantes.
	# Sélections ([['column']]) et renominations (rename).
	# Logique conditionnelle pour filtrer les données.
    
# ============================== Ex04 ============================== #

# Table: Views

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.

 

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filtrer les lignes où l'auteur (author_id) est également le spectateur (viewer_id)
    self_views = views[views['author_id'] == views['viewer_id']]
    # Extraire uniquement les identifiants uniques des auteurs
    authors = self_views[['author_id']].drop_duplicates().sort_values(by='author_id')
    # Renommer la colonne pour correspondre au format attendu
    authors = authors.rename(columns={'author_id': 'id'})
    return authors

# ============================== Ex05 ============================== #

# Table: Tweets

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | tweet_id       | int     |
# | content        | varchar |
# +----------------+---------+
# tweet_id is the primary key (column with unique values) for this table.
# content consists of characters on an American Keyboard, and no other special characters.
# This table contains all the tweets in a social media app.

 

# Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Return the result table in any order.

# The result format is in the following example.

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets = tweets[tweets['content'].str.len() > 15]
    return invalid_tweets[['tweet_id']]
