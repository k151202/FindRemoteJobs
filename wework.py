import requests
from bs4 import BeautifulSoup

def extract_job(html):
    title = html.find("span", {"class": "title"}).get_text()
    company = html.find("span", {"class": "company"}).get_text()
    links = html.find_all("a")
    for item in links:
        if "remote-jobs" in str(item["href"]):
          link = item["href"]
        else:
          continue
    return {"title": title, "company": company, "link": f"https://weworkremotely.com{link}"}

def extract_jobs(url):
    jobs = []
    print("Scrapping Wework...")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("article").find_all("li")
    for result in results[:-1]:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)
    return jobs