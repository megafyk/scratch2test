package meetup

import (
	"testing"
	"time"
)

func TestDay(t *testing.T) {
	println(Day(First, time.Tuesday, time.August, 2023))
}
