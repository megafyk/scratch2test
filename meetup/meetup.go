package meetup

import "time"

type WeekSchedule int

const (
	First  WeekSchedule = 1
	Second              = 8
	Third               = 15
	Fourth              = 22
	Teenth              = 13
	Last                = -6
)

func Day(wSched WeekSchedule, wDay time.Weekday, month time.Month, year int) int {
	if wSched == Last {
		month++
	}
	t := time.Date(year, month, int(wSched), 12, 0, 0, 0, time.UTC)
	return t.Day() + int(wDay-t.Weekday()+7)%7
}

//
//
//type WeekSchedule int
//
//// Define the WeekSchedule type here.
//const (
//	First  WeekSchedule = 0
//	Second              = 7
//	Third               = 14
//	Fourth              = 21
//	Fifth               = 28
//	Teenth              = 14
//	Last                = 28
//)
//
//func Day(wSched WeekSchedule, wDay time.Weekday, month time.Month, year int) int {
//	daysOfMonthOfYear := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
//	if isLeapYear(year) {
//		daysOfMonthOfYear[1] = 29
//	}
//	count := 0
//
//	for i := 0; i < int(month)-1; i++ {
//		count += daysOfMonthOfYear[i]
//	}
//	tempWDayOfMonthOfYear := (365*(year-1) + (year-1)/400 + (year-1)/4 - (year-1)/100 + count) % 7 // if wDayOfMonthOfYear % 7 == 0 -> monday
//	wDayOfMonthOfYear := wDayOfMonthOfYear2wDay(tempWDayOfMonthOfYear)
//	rang := int(wSched)
//	return int(wDay) - int(wDayOfMonthOfYear) + rang + 1
//}
//
//func isLeapYear(year int) bool {
//	if year%400 == 0 {
//		return true
//	}
//	if year%100 == 0 {
//		return false
//	}
//	return year%4 == 0
//}
//
//func wDayOfMonthOfYear2wDay(wDayOfMonthOfYear int) time.Weekday {
//	switch wDayOfMonthOfYear {
//	case 0:
//		return time.Monday
//	case 1:
//		return time.Tuesday
//	case 2:
//		return time.Wednesday
//	case 3:
//		return time.Thursday
//	case 4:
//		return time.Friday
//	case 5:
//		return time.Saturday
//	case 6:
//		return time.Sunday
//	}
//	return time.Monday
//}
