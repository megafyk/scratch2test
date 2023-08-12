package matrix

import (
	"errors"
	"regexp"
	"strconv"
)

type Matrix struct {
	data [][]int
}

func New(s string) (Matrix, error) {
	m := Matrix{}
	var data [][]int

	reRow := regexp.MustCompile("\\n")
	rows := reRow.Split(s, -1)
	reCol := regexp.MustCompile("\\s")

	for i := 0; i < len(rows); i++ {
		cols := reCol.Split(rows[i], -1)
		var tmp []int
		for j := 0; j < len(cols); j++ {
			n, err := strconv.Atoi(cols[j])
			if err != nil {
				return Matrix{}, errors.New("cannot parse string to int data")
			}
			tmp = append(tmp, n)
		}
		data = append(data, tmp)
	}
	m.data = data
	return m, nil
}

// Cols and Rows must return the results without affecting the matrix.
func (m Matrix) Cols() [][]int {
	var mT [][]int
	for i := 0; i < len(m.data[0]); i++ {
		var tmp []int
		for j := 0; j < len(m.data); j++ {
			tmp = append(tmp, m.data[j][i])
		}
		mT = append(mT, tmp)
	}
	return mT
}

func (m Matrix) Rows() [][]int {
	return m.data
}

func (m Matrix) Set(row, col, val int) bool {
	m.data[col][row] = val
	return true
}
