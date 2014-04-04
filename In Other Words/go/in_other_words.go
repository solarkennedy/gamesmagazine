package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "regexp"
import "runtime"

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	hints := Read_hints_file()
	N := len(hints)
	sem := make(chan string);
	for _, hint := range hints {
		hint := hint
		go func (the_hint []string) {
			answers := Start_search(hint)
			sem <- answers;
		} (hint);
	}
	// Wait for all goroutines, and print their answer
	for i := 0; i < N; i++ {
		fmt.Printf("%v\n",<-sem)
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

func Start_search(hint_words []string) (string) {
	words := Import_wordlist()
	_, answers := Search_for_word(hint_words, words)
	return Join_strings(hint_words) + " => " + Join_strings(answers)
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

func Join_strings(string_array []string) (string) {
	return strings.Join(string_array, ", ")
}
