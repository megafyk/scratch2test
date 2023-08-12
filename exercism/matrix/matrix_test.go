package matrix

import (
	"testing"
)

func TestNew(t *testing.T) {
	m, _ := New("9 8 7\n5 3 2\n6 6 7")
	for i := 0; i < len(m.data); i++ {
		for j := 0; j < len(m.data[0]); j++ {
			print(m.data[i][j])
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
