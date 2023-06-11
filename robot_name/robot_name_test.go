package robot_name

import "testing"

func TestRobotName(t *testing.T) {
	robot := new(Robot)
	for i := 0; i < 676001; i++ {
		t, _ := robot.Name()
		print(t)
	}
}
