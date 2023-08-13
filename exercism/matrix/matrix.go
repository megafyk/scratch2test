package matrix

import (
	"errors"
	"regexp"
	"strconv"
)

type Matrix [][]int

func New(s string) (Matrix, error) {
	var m [][]int

	reRow := regexp.MustCompile("\\n")
	rows := reRow.Split(s, -1)
	reCol := regexp.MustCompile("\\s")
	var numCols int
	for i := 0; i < len(rows); i++ {
		cols := reCol.Split(rows[i], -1)
		var tmp []int
		for j := 0; j < len(cols); j++ {
			if cols[j] == "" {
				continue
			}
			n, err := strconv.Atoi(cols[j])
			if err != nil {
				return nil, errors.New("cannot parse string to int data")
			}
			tmp = append(tmp, n)
		}

		if numCols == 0 {
			if len(tmp) == 0 {
				return nil, errors.New("matrix unmatched")
			}
			numCols = len(tmp)
		} else {
			if len(tmp) != numCols {
				return nil, errors.New("matrix unmatched")
			}
		}
		m = append(m, tmp)
	}
	return m, nil
}

// Cols and Rows must return the results without affecting the matrix.
func (m Matrix) Cols() [][]int {
	var mT [][]int
	for i := 0; i < len(m[0]); i++ {
		var tmp []int
		for j := 0; j < len(m); j++ {
			tmp = append(tmp, m[j][i])
		}
		mT = append(mT, tmp)
	}
	return mT
}

func (m Matrix) Rows() [][]int {
	dst := make([][]int, len(m))
	for i := 0; i < len(m); i++ {
		dst[i] = make([]int, len(m[i]))
		copy(dst[i], m[i])
	}
	return dst
}

func (m Matrix) Set(row, col, val int) bool {
	if m == nil || row > len(m)-1 || col > len(m[0])-1 || row < 0 || col < 0 {
		return false
	}
	m[row][col] = val
	return true
}
