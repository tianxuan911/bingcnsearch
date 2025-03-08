"""bingcnsearch is a Python library for searching BingCn, easily."""
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from urllib.parse import unquote
from .user_agents import get_useragent


def _req(term, results, lang, start, proxies, timeout, safe, ssl_verify, region):
    resp = get(
        url="https://cn.bing.com/search",
        headers={
            "User-Agent": get_useragent(),
            "Accept": "*/*"
        },
        params={
            "q": term,
            "count": results + 2,  # Prevents multiple requests
            "first": start,
            "setlang": lang,
            "cc": region,
            "form": "QBRE",
            "safeSearch": safe,
        },
        proxies=proxies,
        timeout=timeout,
        verify=ssl_verify,
    )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(term, num_results=10, lang="zh-CN", proxy=None, advanced=False, sleep_interval=0, timeout=5, safe="Strict", ssl_verify=None, start_num=0, unique=False):
    """Search the Bing search engine"""

    # Proxy setup
    proxies = {"https": proxy, "http": proxy} if proxy and (proxy.startswith("https") or proxy.startswith("http")) else None

    start = start_num
    fetched_results = 0  # Keep track of the total fetched results
    fetched_links = set()  # to keep track of links that are already seen previously

    while fetched_results < num_results:
        # Send request
        resp = _req(term, num_results - start,
                    lang, start, proxies, timeout, safe, ssl_verify, None)
        
        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("li", class_="b_algo")
        new_results = 0  # Keep track of new results in this iteration

        for result in result_block:
            # Find the link tag within the result block
            link_tag = result.find("a", href=True)
            # Find the title tag within the link tag
            title_tag = result.find("h2") if link_tag else None
            # Find the description tag within the result block
            description_tag = result.find("p")

            # Check if all necessary tags are found
            if link_tag and title_tag and description_tag:
                # Extract and decode the link URL
                link = unquote(link_tag["href"]) if link_tag else ""
                # Check if the link has already been fetched and if unique results are required
                if link in fetched_links and unique:
                    continue  # Skip this result if the link is not unique
                # Add the link to the set of fetched links
                fetched_links.add(link)
                # Extract the title text
                title = title_tag.text if title_tag else ""
                # Extract the description text
                description = description_tag.text if description_tag else ""
                # Increment the count of fetched results
                fetched_results += 1
                # Increment the count of new results in this iteration
                new_results += 1
                # Yield the result based on the advanced flag
                if advanced:
                    yield SearchResult(link, title, description)  # Yield a SearchResult object
                else:
                    yield link  # Yield only the link

            if fetched_results >= num_results:
                break  # Stop if we have fetched the desired number of results

        if new_results == 0:
            # If you want to have printed to your screen that the desired amount of queries can not been fulfilled, uncomment the line below:
            # print(f"Only {fetched_results} results found for query requiring {num_results} results. Moving on to the next query.")
            break  # Break the loop if no new results were found in this iteration

        start += 10  # Prepare for the next set of results
        sleep(sleep_interval)
