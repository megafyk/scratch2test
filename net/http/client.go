package main

import (
	"crypto/tls"
	"encoding/json"
	"github.com/rs/zerolog/log"
	"golang.org/x/net/http2"
	"io"
	"net/http"
	"sync"
)

func DataSrcHttps() Data {
	var data Data
	clientSrc := http.Client{
		Transport: &http2.Transport{
			TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
		},
		CheckRedirect: nil,
		Jar:           nil,
		Timeout:       0,
	}

	res, err := clientSrc.Get("https://localhost:8081/src")
	if err != nil {
		log.Err(err).Msg("failed create get request")
		return data
	}

	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			return
		}
	}(res.Body)

	byteData, err := io.ReadAll(res.Body)
	err = json.Unmarshal(byteData, &data)
	if err != nil {
		return data
	}
	return data
}

func DataSrcHttp() Data {
	var data Data
	clientSrc := http.DefaultClient

	res, err := clientSrc.Get("http://localhost:8080/src")
	if err != nil {
		log.Err(err).Msg("failed create get request")
		return data
	}

	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			return
		}
	}(res.Body)

	byteData, err := io.ReadAll(res.Body)
	err = json.Unmarshal(byteData, &data)
	if err != nil {
		return data
	}
	return data
}

func WithOneConnection(data Data) {
	client := &http.Client{}
	var wg sync.WaitGroup

	for i := 0; i < len(data.Items); i++ {
		wg.Add(1)
		resourcePath := data.Items[i]
		req, _ := http.NewRequest("GET", resourcePath, nil)
		req.Header.Set("Cache-Control", "no-cache")
		go func() {
			client.Do(req)
			wg.Done()
		}()
	}

	wg.Wait()
}

func WithMultiConnection(data Data) {
	var wg sync.WaitGroup

	for i := 0; i < len(data.Items); i++ {
		wg.Add(1)
		client := &http.Client{}
		resourcePath := data.Items[i]
		req, _ := http.NewRequest("GET", resourcePath, nil)
		req.Header.Set("Cache-Control", "no-cache")
		go func() {
			client.Do(req)
			wg.Done()
		}()
	}

	wg.Wait()
}
