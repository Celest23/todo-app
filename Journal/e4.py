import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")  #you dont have to add the replace its for space

webbrowser.open("https://www.google.com/search?q=" + user_term)

