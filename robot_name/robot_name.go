package robot_name

import (
	"math/rand"
)

type Robot struct {
	name string
}

var (
	names []string
	tmp   [][]string
)

func init() {
	initNames("", 0)
	tmp = [][]string{names}
}

func (r *Robot) Name() (string, error) {

	if r.name != "" {
		return r.name, nil
	}

	if len(tmp) == 0 {
		return "", nil
	}
	x1 := rand.Intn(len(tmp))
	x2 := rand.Intn(len(tmp[x1]))
	stmp := tmp[x1]
	s := stmp[x2]

	tmp = append(tmp[:x1], tmp[x1+1:]...)

	if len(stmp[:x2]) > 0 {
		tmp = append(tmp, stmp[:x2])
	}
	if len(stmp[x2+1:]) > 0 {
		tmp = append(tmp, stmp[x2+1:])
	}
	r.name = s
	return s, nil
}

func (r *Robot) Reset() {
	tmp = [][]string{names}
	r.name = ""
}

func initNames(seed string, num int) {
	if len(seed) >= 5 {
		names = append(names, seed)
		return
	}
	a := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	b := "0123456789"

	if len(seed) >= 0 && len(seed) < 3 {
		if num >= (len(b) - 1) {
			num = 0
		}
		for i := 0; i < len(b); i++ {
			initNames(string(b[i])+seed, num+1)
		}
	} else if len(seed) >= 3 && len(seed) < 5 {
		if num >= (len(a) - 1) {
			num = 0
		}
		for i := 0; i < len(a); i++ {
			initNames(string(a[i])+seed, num+1)
		}
	}
}
