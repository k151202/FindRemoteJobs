import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

def extract_job(html):
    closed = html.find("td", {"class": "company_and_position"}).find("span", {"class": "closed"})
    try:
      if closed is None:
        title = html.find("td", {"class": "company_and_position"}).find("h2").text
        company = html.find("td", {"class": "company_and_position"}).find("h3").text
        link = html.find("td", {"class": "company_and_position"}).find("a", {"class": "preventLink"})["href"]
        return {"title": title, "company": company, "link": f"https://remoteok.io{link}"}
      else:
        raise Exception
    except Exception as e:
      print("Nothing found from remoteok", e)
      return None
    

def extract_jobs(url):
    jobs = []
    print("Scrapping RemoteOK...")
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr", {"class": "job"})
    if results == []:
      print("Nothing found..")
    else:
      for result in results:
        job = extract_job(result)
        jobs.append(job)
      jobs = list(filter(None, jobs))  
      return jobs

def get_jobs(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs(url)
    return jobs