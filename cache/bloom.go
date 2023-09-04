package cache

import (
	"context"
	"github.com/gocql/gocql"
	"github.com/redis/go-redis/v9"
	"github.com/rs/zerolog/log"
	"github.com/scylladb/gocqlx/v2/table"
	"time"
)

var ctx = context.Background()

type Notify struct {
	ID         int    `db:"id"`
	UserId     string `db:"user_id"`
	NotifyType string `db:"notify_type"`
	Phone      string `db:"phone"`
	CreateTime uint64 `db:"create_time"`
	UpdateTime uint64 `db:"update_time"`
}

var notifyMetadata = table.Metadata{
	Name:    "notify",
	Columns: []string{"id", "user_id", "notify_type", "phone", "create_time", "update_time"},
	PartKey: []string{"id"},
	SortKey: []string{"id"},
}

var notifyTbl = table.New(notifyMetadata)

func BloomCache() {
	// data src
	cluster := gocql.NewCluster("192.168.122.20:9042")
	cluster.Keyspace = "mykeyspace"
	cluster.ConnectTimeout = 60 * time.Second
	session, err := cluster.CreateSession()
	if err != nil {
		log.Err(err)
		return
	}

	var notify []Notify

	q := session.Query(notifyTbl.SelectAll()).Bind(notify)
	q.Release()
	// init cache
	client := redis.NewClusterClient(&redis.ClusterOptions{
		Addrs: []string{"192.168.122.20:6379", "192.168.122.20:6380", "192.168.122.20:6381"},
	})

	key := "abc"
	val := "xyz"

	err = client.Set(ctx, key, val, 0).Err()
	if err != nil {
		log.Err(err)
		return
	}
	log.Info().Msgf("set %s to redis", key)
	res, err := client.Get(ctx, "abc").Result()
	if err != nil {
		log.Err(err)
		return
	}
	log.Info().Msgf("get %s from redis %s", key, res)

}
