package cache

import "testing"

func TestBloomCache(t *testing.T) {
	tests := []struct {
		name string
	}{
		{"run BloomCache test"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			BloomCache()
		})
	}
}
