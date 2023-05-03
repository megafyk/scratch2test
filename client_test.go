package main

import (
	"testing"
)

var httpData Data
var httpsData Data

func init() {
	httpData = DataSrcHttp()
	httpsData = DataSrcHttps()
}

func TestHttpWithOneConnection(t *testing.T) {
	WithOneConnection(httpData)
}

func TestHttpWithMultiConnection(t *testing.T) {
	WithMultiConnection(httpData)
}
