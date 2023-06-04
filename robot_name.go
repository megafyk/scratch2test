package main

import (
	"math/rand"
)

type Robot struct {
	name []string
	tmp  [][]string
}

func (r *Robot) Name() (string, error) {
	if r.tmp == nil {
		r.initNames("", 0)
		r.Reset()
	}

	if len(r.tmp) == 0 {
		return "", nil
	}
	x1 := rand.Intn(len(r.tmp))
	x2 := rand.Intn(len(r.tmp[x1]))
	stmp := r.tmp[x1]
	s := stmp[x2]

	r.tmp = append(r.tmp[:x1], r.tmp[x1+1:]...)

	if len(stmp[:x2]) > 0 {
		r.tmp = append(r.tmp, stmp[:x2])
	}
	if len(stmp[x2+1:]) > 0 {
		r.tmp = append(r.tmp, stmp[x2+1:])
	}

	return s, nil
}

func (r *Robot) Reset() {
	r.tmp = [][]string{r.name}
}

func (r *Robot) initNames(seed string, num int) {
	if len(seed) >= 5 {
		r.name = append(r.name, seed)
		return
	}
	a := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	b := "0123456789"

	if len(seed) >= 0 && len(seed) < 3 {
		if num >= (len(b) - 1) {
			num = 0
		}
		for i := 0; i < len(b); i++ {
			r.initNames(string(b[i])+seed, num+1)
		}
	} else if len(seed) >= 3 && len(seed) < 5 {
		if num >= (len(a) - 1) {
			num = 0
		}
		for i := 0; i < len(a); i++ {
			r.initNames(string(a[i])+seed, num+1)
		}
	}
}

func main() {
	robot := new(Robot)
	for i := 0; i < 676001; i++ {
		t, _ := robot.Name()
		print(t)
	}
}
