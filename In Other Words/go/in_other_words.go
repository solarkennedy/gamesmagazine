package main

import "fmt"
import "bufio"
import "os"
import "strings"

func main() {
	hints := Read_hints_file()
	words := Import_wordlist()
	for _, hint := range hints {
		fmt.Print("Trying to find words that match: ")
		fmt.Println(hint)
		answers := Search_for_word(hint, words)
		fmt.Println("Answers: ")
		fmt.Println(answers)
	}
}

func Import_wordlist() ([]string) {
	words := []string{}
	file, _ := os.Open("/usr/share/dict/words")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		words = append(words, scanner.Text())
	}
	return words
}

func Read_hints_file() ([][]string) {
	hints := [][]string{}
	file, _ := os.Open("hints.txt")
        scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		hint := strings.Split(scanner.Text(), ", ")
		hints = append(hints, hint)
	}
	return hints
}

func Search_for_word(hint []string, words[]string) ([]string) {
	return []string{ "Bogus answer" }
}
