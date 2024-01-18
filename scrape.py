# ----------------------------------------------------------------------
# Name:        scrape.py
# Purpose:     Homework 8 - practice web scraping
#
# Author(s): Paul Chon and Hrishikesh Joshi
# ----------------------------------------------------------------------
"""
This program opens and reads information from the SJSU faculty page.

It systematically compiles information from the SJSU faculty pages
and saves it in a csv file. The information includes last name, first
name, email, phone number, and education information.
"""
import urllib.request
import urllib.error
import bs4
import re
import sys
import os

PEOPLE_URL = 'https://sjsu.edu/people/'

def read_url(url):
    """
    Open the given url and return the corresponding soup object.
    :param url:(string) - the address of the web page to be read
    :return: (Beautiful Soup object) corresponding Beautiful Soup
    object or None if an error is encountered.
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            if not re.match(r'^https://sjsu.edu/people/[a-zA-Z]*',
                            url_file.url):
                return
            url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    except Exception as other_err:  # safer on the web
        print(f'Other error with url: {url}\n{other_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes, 'html.parser')
        return soup

def get_people_links(url):
    """
    Read the given url and return the relevant referenced links.
    :param url:(string) - the address of the faculty index page
    :return: (list of strings) - the relevant people links
    """
    if url is not None:
        soup = read_url(url)
        absolute_links = [urllib.parse.urljoin(url,
                                               anchor.get('href', None))
                          for anchor in soup('a')]
        relevant_links = [link for link in absolute_links
                          if re.match(r'^https://sjsu.edu/people/[a-zA-Z]+',
                                      link)]
        return relevant_links

def extract_name(soup):
    """
    Extract the first and last name from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a tuple of strings representing the first and last names
    """
    h1 = soup('h1')
    if not h1:
        return
    name = h1[0].get_text()
    if ',' in name:
        last, first, *other = name.split(',')
        return last, first
    else:
        first, *last = name.split()
        return last[-1], first

def extract_email(soup):
    """
    Extracts the email from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: string representing email of faculty
    """
    regex = re.compile(r'@[a-zA-Z]*\.[a-zA-Z]*', re.IGNORECASE)
    results = soup.find_all(string=regex)
    if results:
        return results[0]
    return ''

def extract_phone(soup):
    """
    Extracts the phone from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: string representing phone number of faculty (can be in
    different forms)
    """
    h3 = soup('h3')
    telephone_element = None
    for result in h3:
        if result.get_text() == 'Telephone':
            telephone_element = result
        if telephone_element:
            phone_number = telephone_element.find_next().get_text()
            phone_number = re.search(r'\(?\d{3}.*\d{3}.*\d{4}', phone_number)
            if phone_number:
                return phone_number.group()

    return ''

def extract_education(soup):
    """
    Extract the education from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a string representing the education of the faculty/staff
    """
    h2 = soup('h2')
    for result in h2:
        if result.get_text() == 'Education':
            education_element = result.find_next()

            text = ''
            if education_element.name == 'p':
                text = education_element.get_text().strip()
            elif education_element.name == 'ul':
                text = education_element.find('li').text.strip()
            else:
                text = education_element.get_text()

            return ' '.join(text.split()).replace(',', '-')
    return ''

def get_info(url):
    """
    Extract the information from a single faculty/staff web page
    :param url: (string) the address of the faculty/staff web page
    :return: a comma separated string containing: the last name,
    first name, email, phone and education
    """
    soup = read_url(url)
    info = None
    if soup:
        name = extract_name(soup)
        email = extract_email(soup)
        phone = extract_phone(soup)
        education = extract_education(soup)
        if name:
            info = f'{name[0].strip()},{name[1].strip()},{email.strip()}' \
                   f',{phone}' \
                   f',{education}'
    return info

def harvest(url, filename):
    """
    Harvest the information starting from the url specified and write
    that information to the file specified.
    :param url: (string)the main faculty index url
    :param filename: (string) name of the output csv file
    :return: None
    """
    links = get_people_links(url)
    with open(filename, 'w', encoding='UTF-8') as info_file:
        info_file.write('Last Name,First Name,Email,Phone Number,Education\n')
        for link in links:
            info = get_info(link)
            if info:
                info_file.write(info + '\n')


def main():
    if len(sys.argv) != 2:
        print('Error: Invalid number of arguments')
        print('Usage: scrap.py filename')
    else:
        file = sys.argv[1]
        if os.path.splitext(file)[1] == '.csv':
            harvest(PEOPLE_URL, file)
        else:
            print("Please specify a csv filename")


if __name__ == '__main__':
    main()