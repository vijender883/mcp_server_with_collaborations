from mcp.server.fastmcp import FastMCP
import re

# Initialize the MCP server with multiple tools
mcp = FastMCP("MCP-text-analysis",
              host="127.0.0.1",
              port=8080,
              timeout=30)

@mcp.tool()
def count_total_rs(text: str) -> int:
    """Count the total number of Rs in the given string

    Input:
        text: str -> text to count the total number of Rs

    Output:
        count: int -> total number of Rs in the given string
    """

    if not isinstance(text, str):
        raise ValueError("text must be a string")

    return text.lower().count("r")

@mcp.tool()
def count_vowels(text: str) -> dict:
    """Count the number of each vowel in the given string
    
    Input:
        text: str -> text to analyze for vowels
        
    Output:
        counts: dict -> dictionary with the count of each vowel and total
    """
    
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    # Convert to lowercase for case-insensitive counting
    text = text.lower()
    
    # Count each vowel
    vowels = {
        'a': text.count('a'),
        'e': text.count('e'),
        'i': text.count('i'),
        'o': text.count('o'),
        'u': text.count('u')
    }
    
    # Add total count
    vowels['total'] = sum(vowels.values())
    
    return vowels

@mcp.tool()
def analyze_text(text: str) -> dict:
    """Analyze text to provide various statistics
    
    Input:
        text: str -> text to analyze
        
    Output:
        stats: dict -> dictionary with various text statistics
    """
    
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    # Count words
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    
    # Count characters (excluding spaces)
    char_count = len(text.replace(" ", ""))
    
    # Count sentences (simple implementation)
    sentence_count = len(re.split(r'[.!?]+', text)) - 1
    if sentence_count < 0:
        sentence_count = 0
    
    # Calculate average word length
    avg_word_length = round(sum(len(word) for word in words) / max(1, word_count), 2)
    
    # Find most common word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    most_common_word = max(word_freq.items(), key=lambda x: x[1]) if word_freq else ("", 0)
    
    return {
        "word_count": word_count,
        "character_count": char_count,
        "sentence_count": sentence_count,
        "average_word_length": avg_word_length,
        "most_common_word": most_common_word[0],
        "most_common_word_count": most_common_word[1]
    }

@mcp.tool()
def count_specific_character(text: str, character: str) -> int:
    """Count occurrences of a specific character in the given string
    
    Input:
        text: str -> text to analyze
        character: str -> the character to count (only first character is used if multiple are provided)
        
    Output:
        count: int -> number of occurrences of the character
    """
    
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    if not character or not isinstance(character, str):
        raise ValueError("character must be a non-empty string")
    
    # Only use the first character if multiple are provided
    char_to_count = character[0]
    
    return text.lower().count(char_to_count.lower())

@mcp.tool()
def tell_capital_of_country(country: str) -> str:
    """Get the capital of a specific country from a predefined list only.
    
    IMPORTANT: This tool only returns capitals from its internal database.
    Do not supplement the response with external knowledge.
    If the country is not found, return exactly "No data found based on the tool used".
    
    Input:
        country: str -> name of the country to look up
        
    Output:
        capital: str -> capital city of the country from internal database only, 
                       or "No data found based on the tool used" if not in the predefined list
    """
    
    print(f"DEBUG: Input='{country}', Type={type(country)}")
    
    # Dictionary mapping countries to their capitals
    country_capitals = {
        "India": "New Delhi",
        "China": "Peking",
        "United States": "Washington D.C.",
        "United Kingdom": "London",
        "France": "Paris",
        "Germany": "Berlin",
        "Japan": "Tokyo",
        "Australia": "Canberra",
        "Canada": "Ottawa",
        "Brazil": "Brasília"
    }
    
    if not isinstance(country, str):
        raise ValueError("country must be a string")
    
    # Look up the capital (case-insensitive search)
    for country_key, capital in country_capitals.items():
        if country_key.lower() == country.lower():
            print(f"DEBUG: Found match, returning '{capital}'")
            return capital
    
    print(f"DEBUG: No match found for '{country}'")
    return "No data found based on the tool used"

@mcp.tool()
def find_longest_word(text: str) -> dict:
    """Find the longest word in the given text
    
    Input:
        text: str -> text to analyze
        
    Output:
        result: dict -> dictionary with the longest word and its length
    """
    
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    # Find all words
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return {"longest_word": "", "length": 0}
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    return {
        "longest_word": longest_word,
        "length": len(longest_word)
    }


if __name__ == "__main__":
    print("Starting MCP Text Analysis server at http://127.0.0.1:8080")
    print("Available tools:")
    print("- count_total_rs: Count occurrences of 'r' in text")
    print("- count_vowels: Count each vowel in text")
    print("- analyze_text: Provide comprehensive text statistics")
    print("- count_specific_character: Count occurrences of a specified character")
    print("- tell_capital_of_country: Get capital from predefined list only")
    print("- find_longest_word: Find the longest word in the text")
    mcp.run()