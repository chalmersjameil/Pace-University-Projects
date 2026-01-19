def main():
    city_names = ["Toronto", "Ottawa", "Vancouver", "Montreal", "Calgary", "Edmonton", "Winnipeg", "Quebec City", "Hamilton", "Kitchener", "Philadelphia"]
    
    def count_vowels(city_name):
        vowels = 'aeiou'
        return sum(1 for char in city_name.lower() if char in vowels)

    largest_vowel_city = max(city_names, key=count_vowels)
    vowel_count = count_vowels(largest_vowel_city)

    print(f"The city with the largest number of vowels is {largest_vowel_city} with {vowel_count} vowels.")
    
if __name__ == '__main__':
    main()
