module scratch2test

go 1.20

require (
	github.com/gorilla/websocket v1.5.0
	github.com/redis/go-redis/v9 v9.1.0
	github.com/rs/zerolog v1.29.1
	golang.org/x/net v0.9.0
)

require (
	github.com/cespare/xxhash/v2 v2.2.0 // indirect
	github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f // indirect
	github.com/gocql/gocql v1.6.0 // indirect
	github.com/golang/snappy v0.0.4 // indirect
	github.com/hailocab/go-hostpool v0.0.0-20160125115350-e80d13ce29ed // indirect
	github.com/mattn/go-colorable v0.1.12 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/scylladb/go-reflectx v1.0.1 // indirect
	github.com/scylladb/gocqlx/v2 v2.8.0 // indirect
	golang.org/x/sys v0.7.0 // indirect
	golang.org/x/text v0.9.0 // indirect
	gopkg.in/inf.v0 v0.9.1 // indirect
)

replace github.com/gocql/gocql => github.com/scylladb/gocql v1.11.1
