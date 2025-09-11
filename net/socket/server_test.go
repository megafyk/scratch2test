package socket

import "testing"

func TestStart(t *testing.T) {
	tests := []struct {
		name string
	}{
		{"start server"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			Start()
		})
	}
}
