package socket

import (
	"fmt"
	"github.com/gorilla/websocket"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"net/http"
)

var upgraderBase = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		// Allow all connections by returning true
		return true
	},
}

func Start() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	port := "8080"

	hub := newHub()
	go hub.run()
	mux := http.NewServeMux()

	mux.HandleFunc("/wsBase", func(writer http.ResponseWriter, request *http.Request) {
		conn, err := upgraderBase.Upgrade(writer, request, nil)
		if err != nil {
			log.Err(err)

			return
		}

		defer func(conn *websocket.Conn) {
			err := conn.Close()

			if err != nil {
				log.Err(err)
				return
			}

			log.Info().Msgf("closed connection from %s", conn.RemoteAddr())
		}(conn)

		for {
			// Read message from the client
			_, message, err := conn.ReadMessage()
			if err != nil {
				log.Err(err)
				break
			}

			log.Info().Msgf("Received message from client: %s", message)

			// Write a response back to the client
			response := []byte("This is the server's response")
			err = conn.WriteMessage(websocket.TextMessage, response)

			if err != nil {
				log.Err(err)
				break
			}
		}

	})

	mux.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
		log.Info().Msgf("init ws from %s", r.RemoteAddr)
		serveWs(hub, w, r)
		log.Info().Msgf("finish create ws %s", r.RemoteAddr)
	})

	go func() {
		err := http.ListenAndServe(fmt.Sprintf(":%s", port), mux)
		if err != nil {
			log.Fatal().Err(err).Msgf("failed start server at port %s", port)
		}
	}()

	done := make(chan bool)
	log.Info().Msgf("server started")
	<-done
	close(done)
}
