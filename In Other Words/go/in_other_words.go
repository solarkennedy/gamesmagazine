package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "regexp"

func main() {
	hints := Read_hints_file()
	words := Import_wordlist()
	N := len(hints)
	sem := make(chan []string, N);  // semaphore pattern
	for _, hint := range hints {
		go func (the_hint []string) {
			fmt.Print("Trying to find words that match: ")
			fmt.Println(hint)
			_, answers := Search_for_word(hint, words)
			sem <- answers;
		} (hint);
	}
	// Wait for all goroutines
	for i := 0; i < N; i++ {
		<-sem
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
		return hint_words, words
	} else if len(hint_words) == 0 {
		return hint_words, words
	} else {
		word := hint_words[0]
		matching_words := []string{}
		hint_array := strings.Split(word, "")
		regex_string := strings.ToLower(".*" + strings.Join(hint_array, ".*") + ".*")
		word_regex, _ := regexp.Compile(regex_string)
		for _, dict_word := range words {
			match := word_regex.MatchString(dict_word)
			if match {
				matching_words = append(matching_words, dict_word)
			}
		}
		return Search_for_word(hint_words[1:], matching_words)
	}
}
