import asyncio
import time
import requests
import httpx

urls = [
"https://example.com/tech-seo-vercel-gcp/z",
"https://example.com/firebase-django-ruby/S",
"https://example.com/docker-css-css/E",
"https://example.com/git-mysql-sitemap/q",
"https://example.com/performance-cdn-conversion-rate/4",
"https://example.com/azure-joomla-mvc/A",
"https://example.com/performance-sitemap-aws/U",
"https://example.com/drupal-server-bounce-rate/H",
"https://example.com/scrum-prototype-laravel/K",
"https://example.com/frontend-performance-azure/8",
]

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print(f"{func.__name__:30} {(t2 - t1):.2f}")
    return inner

@timer
def run_nothing():
    pass

@timer
def run_requests():
    results = [requests.get(url) for url in urls]

@timer
def run_requests_session():
    s = requests.session()
    results = [s.get(url) for url in urls]

async def httpx_async():
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(client.get(url)) for url in urls]
        await asyncio.gather(*tasks)

@timer
def run_httpx_async():
    asyncio.run(httpx_async())


if __name__ == "__main__":
    run_nothing()
    run_requests()
    run_requests_session()
    run_httpx_async()


# A good example for async is web scraping. 
# If you’re accessing multiple websites, most of the time you’re waiting for the following:

# Client request → server (I/O)
# Server (processing your request; now where did I put that file again?)
# Server results → client (I/O)

## Most major web frameworks include these tasks:

# Handle HTTP
# Perform authentication (authn, or who are you?)
# Perform authorization (authz, or what can you do?)
# Manage sessions
# Get parameters
# Validate parameters (required/optional, type, range)
# Handle HTTP verbs
# Route (functions/classes)
# Serve static files (HTML, JS, CSS, images)
# Serve dynamic data (databases, services)
# Return values and HTTP status

## Optional features include the following:

# Backend templates
# Database connectivity, ORMs
# Rate limiting
# Asynchronous tasks
