package wordy

import (
	"regexp"
	"strconv"
	"strings"
)

func Answer(question string) (int, bool) {
	question = strings.ToLower(question)
	question = strings.ReplaceAll(question, "by", "")
	question = strings.ReplaceAll(question, "?", "")
	re := regexp.MustCompile("\\s+")
	words := re.Split(question, -1)
	if len(words) < 3 || "what" != words[0] || "is" != words[1] || len(words)%2 == 0 {
		return 0, false
	}

	var res int

	var err error
	res, err = strconv.Atoi(words[2])
	if err != nil {
		return 0, false
	}

	for i := 3; i < len(words)-1; i++ {
		if !checkop(words[i]) {
			return 0, false
		}
		x, err := strconv.Atoi(words[i+1])
		if err != nil {
			return 0, false
		}
		res = op(words[i], res, x)
		i++
	}

	return res, true
}

func checkop(str string) bool {
	return str == "plus" || str == "minus" || str == "multiplied" || str == "divided"
}

func op(op string, a int, b int) int {
	switch op {
	case "plus":
		return a + b
	case "minus":
		return a - b
	case "multiplied":
		return a * b
	case "divided":
		return a / b
	}
	return 0
}
