package tree_building

import "errors"

type Record struct {
	ID     int
	Parent int
	// feel free to add fields as you see fit
}

type Node struct {
	ID       int
	Children []*Node
	// feel free to add fields as you see fit
}

func Build(records []Record) (*Node, error) {
	if len(records) == 0 {
		return nil, errors.New("empty")
	}
	records = MergeSort0(records)
	root := &Node{records[0].ID, nil}
	queue := append([]*Node{}, root)
	t := 1
	for true {
		if len(queue) == 0 {
			break
		}
		r := queue[0]
		queue = queue[1:]
		var child []*Node
		for i := t; i < len(records); i++ {
			if records[i].Parent == r.ID {
				node := &Node{records[i].ID, nil}
				child = append(child, node)
				queue = append(queue, node)
			}
		}
		t += 1
		r.Children = child
	}
	return root, nil
}

func MergeSort0(slice []Record) []Record {
	if len(slice) < 2 {
		return slice
	}
	mid := (len(slice)) / 2
	return Merge(MergeSort0(slice[:mid]), MergeSort0(slice[mid:]))
}
func Merge(left, right []Record) []Record {

	size, i, j := len(left)+len(right), 0, 0
	slice := make([]Record, size, size)

	for k := 0; k < size; k++ {
		if i > len(left)-1 && j <= len(right)-1 {
			slice[k] = right[j]
			j++
		} else if j > len(right)-1 && i <= len(left)-1 {
			slice[k] = left[i]
			i++
		} else if left[i].ID < right[j].ID {
			slice[k] = left[i]
			i++
		} else {
			slice[k] = right[j]
			j++
		}
	}
	return slice
}

func printRecords(records []Record) {
	for i := 0; i < len(records); i++ {
		print(records[i].ID)
	}
	println("")
}
