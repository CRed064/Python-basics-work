import pandas as pd

# Q1

data = pd.read_csv('Test_Pandas.csv')
columns = data.columns

print "\n Q1 \n"

print "All column names \n"
print columns
# print type(columns)

# Q2

print "\n Q2\n"

# a. How many unique shops are in the dataset? Shopid
n_unique_shops = data.shopid.nunique()

print "a. There are %d unique shops." % n_unique_shops

# b. How many unique preferred and cross border shops? is_preferred, cb_option
preferred = data[data.is_preferred == True]
cb = data[data.cb_option == True]

n_unique_preferred = preferred.shopid.nunique()
n_unique_cb = cb.shopid.nunique()

print "b. There are %d unique preferred and %d unique cross border shops." \
% (n_unique_preferred, n_unique_cb)

# c. How many products have zero sold count? sold_count
zero_sc = data[data.sold_count == 0].itemid.nunique()
print "c. %d products have zero sold count." % zero_sc

# d. How many products were created in the year 2018? item_creation_date
data['item_creation_year'] = data.item_creation_date.apply(lambda x: x.split\
(' ')[0].split('/')[2])

year_2018_products = data[data.item_creation_year == '2018'].itemid.count()
print "d. %d products were created in the year 2018." % year_2018_products

# Q3

print "\n Q3 \n"

# a. Top 3 preferred shops' shopid , largest number of unique products
# nunique()
df = preferred.groupby('shopid').itemid.nunique().reset_index().sort_values\
(by = 'itemid', ascending = False)
# df.rename(columns = {'itemid': 'Number of unique products'})
print "Top 3 preferred shops' shopid, with number of unique products \n"
print df.head(3), '\n'

# b. Top 3 categories, largest number of unique cross border products
# nunique()
df1 = cb.groupby('category').itemid.nunique().reset_index().sort_values\
(by = 'itemid', ascending = False)
print "Top 3 categories, with number of unique cross border products \n"
print df1.head(3), '\n'

# Q4 Top 3 shopid with the highest revenue

print "\n Q4 \n"

data['revenue'] = data.price * data.stock
df2 = data.groupby('shopid').revenue.sum().reset_index().sort_values\
(by = 'revenue', ascending = False)
print "Top 3 shopid with the highest revenue \n"
print df2.head(3), '\n'

# Q5 Number of products that have more than 3 variations
# nunique()

print "\n Q5 \n"

df3 = data.groupby('itemid').item_variation.nunique().reset_index().sort_values\
(by = 'item_variation', ascending = False)
# print df3.head(10), '\n'
df4 = df3[df3.item_variation > 3]
print df4.itemid.count(), '\n'

# Q6 Duplicated listings within each shop

print "\n Q6 \n"

# a.
data['is_duplicated'] = data.duplicated(subset = ['item_name', \
'item_description', 'price'], keep = False)

# print data.head(5)

# b.
duplicated_listings = data[(data.is_duplicated == True) & (data.sold_count < 2)]

# writing to Excel .xlsx file
# writer = pd.ExcelWriter('duplicated_listings.xlsx')
# duplicated_listings.to_excel(writer)
# writer.save()

# c. preferred shopid with the most duplicate listings
