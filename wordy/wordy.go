package wordy

import (
	"errors"
	"strconv"
	"strings"
)

type Node struct {
	value string
	left  *Node
	right *Node
}

func Answer(question string) (int, bool) {
	question = strings.ToLower(question)
	words := strings.Split(question, " ")
	if len(words) < 3 || "what" != words[0] || "is" != words[1] {
		return 0, false
	}

	words[len(words)-1] = strings.ReplaceAll(words[len(words)-1], "?", "")

	var root Node
	numbered := 0
	prev := root

	nextIsNumber := true
	// build tree
	for i := 2; i < len(words); i++ {
		if nextIsNumber {
			_, err := strconv.Atoi(words[i])
			if err != nil {
				return 0, false
			}
			node := Node{words[i], nil, nil}
			if root.value == "" {
				root = node
			} else {
				prev.right = &node
			}
			prev = node
			nextIsNumber = false
		} else {
			if operator(words[i]) {
				if words[i] == "plus" || words[i] == "minus" {
					node := Node{words[i], &prev, nil}
					prev = node
					root = node
				} else {
					tmp := prev.value
					prev.value = words[i]
					node := Node{tmp, nil, nil}
					prev.left = &node
				}
			} else {
				return 0, false
			}
			nextIsNumber = true
		}
		numbered++
	}
	if numbered%2 == 0 {
		return 0, false
	}

	n, err := strconv.Atoi(root.value)
	if err != nil {
		return 0, false
	}
	return n, true
}

func operator(str string) bool {
	return str == "plus" || str == "minus" || str == "multiplied" || str == "divided"
}

func operate(op string, a int, b int) (int, error) {
	switch op {
	case "plus":
		return a + b, nil
	case "minus":
		return a - b, nil
	case "multiplied":
		return a * b, nil
	case "divided":
		return a / b, nil
	default:
		return 0, errors.New("operator does not supported")
	}
}
