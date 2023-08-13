package matrix

import (
	"testing"
)

func TestNew(t *testing.T) {
	m, _ := New("1 2 3\n4 5 6\n7 8 9\n 8 7 6")
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[0]); j++ {
			print(m[i][j])
			print(" ")
		}
		println()
	}
	println()
	for i := 0; i < len(m.Cols()); i++ {
		for j := 0; j < len(m.Cols()[0]); j++ {
			print(m.Cols()[i][j])
			print(" ")
		}
		println()
	}
}
