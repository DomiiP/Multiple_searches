import webbrowser
import sys

# --- | (1) Simple command program for multiple searches (with parameters)| ---

if __name__ == "__main__":
    # Words
    try:
        words  = sys.argv[1]
    except Exception as e:
        print(e)
    try:
        before = sys.argv[2]
    except Exception as e:
        print(e)
    try:
        after  = sys.argv[3]
    except Exception as e:
        print(e)
    print(f'This is a test print of words: {words}, and also of before: {before} and of after: {after}')
    
# For easier implementation I will just use Google
browser = 'google'
# This will not be implemented in command program
specified_browser = 'chrome'

# Logic behind it
for word in words:
    # Google
    if(list_of_enabled_browsers[0]):
        webbrowser.open(f"https://google.com/search?q={static_before_word}+{word}+{static_after_word}")
    # DuckDuckGo
    if(list_of_enabled_browsers[1]):
        webbrowser.open(f"https://duckduckgo.com/?q={static_before_word}+{word}+{static_after_word}")
    # Bing
    if(list_of_enabled_browsers[2]):
        webbrowser.open(f"https://bing.com/search?q=={static_before_word}+{word}+{static_after_word}")
