import webbrowser

# Basic command
#webbrowser.open("https://google.com")

# --- | (1) Simple command program for multiple searches (without program paramaters)| ---

# Variables
static_before_word = 'Red'
static_after_word  = ''
list_of_words = ['Couch','dog', 'cat']
                          #Google DuckDuckGo Bing
list_of_enabled_browsers = [True,   False   ,False ]
# This will not be implemented in command program
specified_browser = 'chrome'

# Logic behind it
for word in list_of_words:
    # Google
    if(list_of_enabled_browsers[0]):
        webbrowser.open(f"https://google.com/search?q={static_before_word}+{word}+{static_after_word}")
    # DuckDuckGo
    if(list_of_enabled_browsers[1]):
        webbrowser.open(f"https://duckduckgo.com/?q={static_before_word}+{word}+{static_after_word}")
    # Bing
    if(list_of_enabled_browsers[2]):
        webbrowser.open(f"https://bing.com/search?q=={static_before_word}+{word}+{static_after_word}")
