package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "regexp"

func main() {
	hints := Read_hints_file()
	words := Import_wordlist()
	for _, hint := range hints {
		fmt.Print("Trying to find words that match: ")
		fmt.Println(hint)
		_, answers := Search_for_word(hint, words)
		fmt.Println("Answers: ")
		fmt.Println(answers)
	}
}

func Import_wordlist() []string {
	words := []string{}
	file, _ := os.Open("/usr/share/dict/words")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		words = append(words, scanner.Text())
	}
	return words
}

func Read_hints_file() [][]string {
	hints := [][]string{}
	file, _ := os.Open("hints.txt")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		hint := strings.Split(scanner.Text(), ", ")
		hints = append(hints, hint)
	}
	return hints
}

func Search_for_word(hint_words []string, words []string) ([]string, []string) {
	if len(hint_words) == 0 {
		fmt.Println("DEBUG: Out of hints")
		return []string{}, []string{}
	} else if len(hint_words) == 0 {
		fmt.Println("DEBUG: Out of hints")
		return []string{}, []string{}
	} else {
		word := hint_words[0]
		fmt.Println("Searching all words for " + word)
		matching_words := []string{}
		word_regex := word
		for _, dict_word := range words {
			match, _ := regexp.MatchString(word_regex, dict_word)
			if match {
				matching_words = append(matching_words, dict_word)
			}
		}
		return Search_for_word(hint_words[1:], matching_words)
	}
}
