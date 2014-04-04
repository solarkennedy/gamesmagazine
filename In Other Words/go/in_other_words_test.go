package main

import "testing"
import "reflect"

func TestRead_hints_file(t *testing.T) {
	hints := Read_hints_file()
	expected := []string{"ANT", "CHAT", "ERA", "MEAT", "RAN"}
	actual := hints[0]
	if !reflect.DeepEqual(actual, expected) {
		t.Log(actual)
		t.Log(expected)
		t.Error("Actual and expected differ ^")
	}
}

func TestSearch_for_word(t *testing.T) {
	hint := []string{"ANT", "CHAT", "ERA", "MEAT", "RAN"}
	words := []string{"bogus", "test_string", "merchant", "merchants"}
	_, actual := Search_for_word(hint, words)
	expected := []string{"merchant", "merchants"}
	if !reflect.DeepEqual(actual, expected) {
		t.Log(actual)
		t.Log(expected)
		t.Error("Actual and expected differ ^")
	}
}

func TestJoin_strings(t *testing.T) {
	words := []string{"bogus", "test_string", "merchant", "merchants"}
	expected := "bogus, test_string, merchant, merchants"
	actual := Join_strings(words)
	if expected != actual {
		t.Log(actual)
		t.Log(expected)
		t.Error("Actual and expected differ ^")
	}
}


func BenchmarkImport_wordlist(b *testing.B) {
	for n := 0; n < b.N; n++ {
		Import_wordlist()
	}
}
