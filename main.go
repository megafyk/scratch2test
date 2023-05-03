package main

import (
	"encoding/json"
	"fmt"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"html/template"
	"net/http"
	"os"
)

func main() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	portHttp := "8080"
	portHttps := "8081"

	mux := http.NewServeMux()
	mux.HandleFunc("/", GetHomepage)
	mux.HandleFunc("/src", GetHomeResource)

	fs := http.FileServer(http.Dir("./assets"))
	mux.Handle("/assets/", http.StripPrefix("/assets/", fs))

	go func() {
		err := http.ListenAndServe(fmt.Sprintf(":%s", portHttp), mux)
		if err != nil {
			log.Fatal().Err(err).Msgf("failed start http server at port %s", portHttps)
		}
	}()

	go func() {
		err := http.ListenAndServeTLS(fmt.Sprintf(":%s", portHttps), "server.crt", "server.key", mux)
		if err != nil {
			log.Fatal().Err(err).Msgf("failed start https server at port %s", portHttps)
		}
	}()

	done := make(chan bool)
	log.Info().Msgf("server started")
	<-done
	close(done)
}

func GetHomepage(w http.ResponseWriter, r *http.Request) {
	log.Info().Msg("GetHomepage")

	files, _ := os.ReadDir("./assets/")
	var items []string
	var data []Data

	for i := 0; i < len(files); i++ {
		log.Info().Msgf(files[i].Name())
		if i%3 == 0 {
			if len(items) > 0 {
				data = append(data, Data{Items: items})
			}
			items = []string{}
		}
		items = append(items, files[i].Name())
	}
	if len(items) > 0 {
		data = append(data, Data{Items: items})
	}

	parseFiles, _ := template.ParseFiles("index.html")

	err := parseFiles.Execute(w, data)
	if err != nil {
		log.Err(err).Msg("failed render page")
	}
}

func GetHomeResource(w http.ResponseWriter, r *http.Request) {
	files, _ := os.ReadDir("./assets/")
	var resourceList []string
	for i := 0; i < len(files); i++ {
		resourceList = append(resourceList, fmt.Sprintf("%s://%s/assets/%s", GetScheme(r), r.Host, files[i].Name()))
	}
	log.Info().Msg("GetHomeResource")
	b, err := json.Marshal(Data{Items: resourceList})
	if err != nil {
		log.Err(err).Msg("Failed parse json")
		w.WriteHeader(http.StatusInternalServerError)
	}
	w.Header().Set("Content-Type", "application/json")
	_, err = w.Write(b)
	if err != nil {
		return
	}
}

func GetScheme(r *http.Request) string {
	if r.TLS == nil {
		return "http"
	} else {
		return "https"
	}
}
