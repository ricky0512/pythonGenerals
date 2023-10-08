from bs4 import BeautifulSoup

# def extractElementsByClass(htmlFile, class_name):
#     # Open the HTML file and parse it using BeautifulSoup
#     with open(htmlFile, 'r', encoding='utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')

#     # Find all elements with the specified class name
#     elements = soup.find_all(class_=class_name)

#     # Extract the text or other attributes from the elements
#     extracted_data = [element.get_text() for element in elements]

#     return extracted_data

def extractHtmlByClass(file_path, class_name):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Find all elements with the specified class name
    elements = soup.find_all(class_=class_name)

    # Create a new BeautifulSoup object to store the extracted content
    extracted_soup = BeautifulSoup("", 'lxml')

    # Add the elements with the specified class name to the new BeautifulSoup object
    for element in elements:
        extracted_soup.append(element)

    # Convert the extracted_soup back to a string with original formatting
    extracted_html = extracted_soup.prettify()

    return extracted_html

def extractFirstTbody(html):
    # Parse the extracted HTML content
    soup = BeautifulSoup(html, 'lxml')

    # Find the first <tbody> element
    first_tbody = soup.find('tbody')

    # If a <tbody> element is found, convert it to a string
    if first_tbody:
        tbody_html = str(first_tbody)
        return tbody_html
    else:
        return None

def extract2ndTbody(html_content):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Find all tbody elements
    tbody_elements = soup.find_all('tbody')

    # Check if there are at least two tbody elements
    if len(tbody_elements) >= 2:
        # Extract the second tbody element
        second_tbody = tbody_elements[1]

        # Convert the second tbody to a string with original formatting
        second_tbody_html = second_tbody.prettify()

        return second_tbody_html
    else:
        return None

def extractTrsAndTdValues(html_content):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Find all <tr> elements
    tr_elements = soup.find_all('tr')

    data_dict_list = []

    # Loop through each <tr> element
    for tr in tr_elements:
        td_elements = tr.find_all('td')

        # Extract the text from <td> elements and store in a dictionary
        td_values = {}
        for td in td_elements:
            field_name = td.get('field')  # Assuming 'field' is an attribute in the <td> elements
            if field_name:
                # td_values[field_name] = td.get_text()
                td_text = td.get_text().strip()  # Trim whitespace and newline characters
                td_values[field_name] = td_text

        # Append the dictionary to the list
        data_dict_list.append(td_values)

    return data_dict_list

outF = 'c:\somwhere\fName.html'
targetClass = 'className'

extractedHtml = extractHtmlByClass(outF, targetClass)

secondTbodyHtml = extract2ndTbody(extractedHtml)

dataset = extractTrsAndTdValues(secondTbodyHtml)
print(f"dataset: {dataset}")
