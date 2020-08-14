# saikiran_DyNotify_tasks

This script is used for scraping the product details from the amazon website and store in the JSON file.

I retrieved data from all webpages related that product and stored in JSON file with the unique filename in format "data"+product_name

Some of the issues while scraping product details from amazon. Since Amazon is smart it raises an error when accessing the data 
from a third party.

It raises an error as following:- 
 ["Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies"]

Since it blocks as to scrape data from a third party(like using Beautifulsoap) it provides an API were 
 we can retrieve data from amazon API and show in our on the website , link for information related to that is given below:

https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html
