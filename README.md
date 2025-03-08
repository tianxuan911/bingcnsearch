# Bingcnsearcn
Bingcnsearcn is a Python library for searching cn.bing.com, easily. Bingcnsearcn uses requests and BeautifulSoup4 to scrape cn.bing.com. 

## Installation
To install, run the following command:
```bash
python3 -m pip install bingcnsearcn-python
```

## Usage
To get results for a search term, simply use the search function in bingcnsearcn. For example, to get results for "Bing" in cn.bing.com, just run the following program:
```python
from bingcnsearcn import search
search("Bing")
```

## Additional options
Bingcnsearcn supports a few additional options. By default, bingcnsearcn returns 10 results. This can be changed. To get a 100 results on cn.bing.com for example, run the following program.
```python
from bingcnsearcn import search
search("Bing", num_results=100)
```
If you want to have unique links in your search result, you can use the `unique` option as in the following program.
```python
from bingcnsearcn import search
search("Bing", num_results=100, unique=True)
```
In addition, you can change the language([Lanaguage Codes](https://learn.microsoft.com/zh-cn/bing/search-apis/bing-web-search/reference/market-codes#bing-supported-language-codes)) bing searches in. For example, to get results in French run the following program:
```python
from bingcnsearcn import search
search("Bing", lang="fr")
```
You can also specify the region ([Country Codes](https://learn.microsoft.com/zh-cn/bing/search-apis/bing-web-search/reference/market-codes#country-codes)) for your search results. For example, to get results specifically from the US run the following program:
```python
from bingcnsearcn import search
search("Bing", region="us")
```
If you want to turn off the safe search function (this function is on by default), you can do this:
```python
from bingcnsearcn import search
search("Bing", safe="Off")
```
To extract more information, such as the description or the result URL, use an advanced search:
```python
from bingcnsearcn import search
search("Bing", advanced=True)
# Returns a list of SearchResult
# Properties:
# - title
# - url
# - description
```
If requesting more than 100 results, bingcnsearcn will send multiple requests to go through the pages. To increase the time between these requests, use `sleep_interval`:
```python
from bingcnsearcn import search
search("Bing", sleep_interval=5, num_results=200)
```

```
If requesting more than 10 results, but want to manage the batching yourself? 
Use `start_num` to specify the start number of the results you want to get:
```python
from bingcnsearcn import search
search("Bing", sleep_interval=5, num_results=200, start_result=10)
```

If you are using a HTTP Rotating Proxy which requires you to install their CA Certificate, you can simply add `ssl_verify=False` in the `search()` method to avoid SSL Verification.
```python
from bingcnsearcn import search


proxy = 'http://username:password@proxy.host.com:8080/'
# or for socks5
# proxy = 'socks5://username:password@proxy.host.com:1080/'

j = search("proxy test", num_results=100, lang="en", proxy=proxy, ssl_verify=False)
for i in j:
    print(i)
```
