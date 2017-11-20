# SeekingAlphaCrawler
A web crawler focus on the seeking alpha website

## webdriver for the Seeking Alpha
The articles in the Seeking Alpha is triggered by scrolling, thus at first I use webdriver to simulate the action of scrolling, selenium is one of the choice. However, the webpage keeps refreshing itself which makes the extraction of webpage links hard. After finding the static pages of the Seeking Alpha extract to show articles, I turn to BeautifulSoup to parse HTML.

## bs4 Crawler for the Seeking Alpha
The static page link contains articles is:
```python
url = 'https://seekingalpha.com/symbol/'+ symbol + '/more_focus?page=' + str(page_number)
```
After extracting links of articles in the static pages and saving into variable `link_list` with function `search_links` and `save_links` respectively, I extract summary by parsing links one by one and save them into file with function `extract_summary` and `save_to_excel`. 

For more information, please see the details in [bs4Crawler.py](bs4Crawler.py).
