package cryptosquare

import (
	"math"
	"regexp"
	"strings"
)

func Encode(pt string) string {
	var mx [][]string
	var mxT [][]string



	re := regexp.MustCompile("\\W")
	pt = re.ReplaceAllString(pt, "")
	pt = strings.ToLower(pt)
	if len(pt) == 0 {
		return pt
	}
	m := int(math.Sqrt(float64(len(pt))))
	n := m
	plusM := true
	for m * n < len(pt) {
		if plusM {
			m++
		} else {
			n++
		}
		plusM = !plusM
	}


	var tmp []string
	for i := 0; i < len(pt); i++ {
		tmp = append(tmp, string(pt[i]))
		if (i+1)%m == 0 {
			mx = append(mx, tmp)
			tmp = []string{}
		}
	}
	mx = append(mx, tmp)

	i := 0
	for i < m {
		var tmp []string
		for j := 0; j < n; j++ {
			if i < len(mx[j]) {
				tmp = append(tmp, mx[j][i])
			} else {
				tmp = append(tmp, " ")
			}
			if j == n-1 {
				mxT = append(mxT, tmp)
				tmp = []string{}
			}
		}
		i++
	}

	res := ""
	for i := 0; i < len(mxT); i++ {
		for j := 0; j < len(mxT[i]); j++ {
			res += mxT[i][j]
		}
		res += " "
	}
	return res[:len(res)-1]
}
