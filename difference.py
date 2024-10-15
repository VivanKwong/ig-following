from bs4 import BeautifulSoup

# Helper function to extract names/IDs from the HTML files
def extract_names_from_html(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Assuming names are in the href text or in the <a> tag text
        return [a.get_text().strip() for a in soup.find_all('a')]

# Extract following and followers
following = extract_names_from_html('filename1.html') # Change to the path to your following HTML file
followers = extract_names_from_html('filename2.html') # Change to the path to your followers HTML file

# Find people you're following but who aren't following you back
not_following_back = [person for person in following if person not in followers]

# Output the result
print("People who are not following you back:")
for person in not_following_back:
    print(person)
