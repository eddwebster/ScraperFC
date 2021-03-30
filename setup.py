import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'ScraperFC',
    version = '0.1.15',
    author = 'Owen Seymour',
    author_email = 'osmour043@gmail.com',
    description = 'Package for scraping soccer data from a variety of sources.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/oseymour/ScraperFC',
#     packages = setuptools.find_packages(),#include=['ScraperFC', 'ScraperFC.*']),
#     py_modules=['FBRef','FiveThirtyEight','Main','shared_functions','Understat'],
    package_dir = {"":"code"},
    packages = setuptools.find_packages(where="code"),
    keywords = ["soccer","football","Premier League","Serie A",
                "La Liga","Bundesliga","Ligue 1"],
    classifiers = [
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.6'
)
  