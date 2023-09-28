package cache

import (
	"context"
	"github.com/gocql/gocql"
	"github.com/redis/go-redis/v9"
	"github.com/rs/zerolog/log"
	"github.com/scylladb/gocqlx/v2"
	"github.com/scylladb/gocqlx/v2/table"
	"time"
)

var ctx = context.Background()

type Notify struct {
	ID         int       `db:"id"`
	UserId     string    `db:"user_id"`
	NotifyType string    `db:"notify_type"`
	Phone      string    `db:"phone"`
	CreateTime time.Time `db:"create_time"`
	UpdateTime time.Time `db:"update_time"`
}

type Transaction struct {
	Step           int     `db:"step"`
	Type           string  `db:"type"`
	Amount         float64 `db:"amount"`
	NameOrig       string  `db:"nameOrig"`
	OldBalanceOrg  float64 `db:"oldbalanceOrg"`
	NewBalanceOrig float64 `db:"newbalanceOrig"`
	NameDest       string  `db:"nameDest"`
	OldBalanceDest float64 `db:"oldbalanceDest"`
	NewBalanceDest float64 `db:"newbalanceDest"`
	IsFraud        int     `db:"isFraud"`
	IsFlaggedFraud int     `db:"isFlaggedFraud"`
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
	cluster.Consistency = gocql.One

	session, err := gocqlx.WrapSession(cluster.CreateSession())
	if err != nil {
		log.Err(err).Msg("cannot create db session")
		return
	}

	defer session.Close()

	var notify []Notify
	q := session.Query(notifyTbl.SelectAll())
	if err := q.SelectRelease(&notify); err != nil {
		log.Err(err).Msg("cannot run query")
		return
	}

	for i := 0; i < len(notify); i++ {
		log.Info().Msgf("id=%d user_id=%s", notify[i].ID, notify[i].UserId)
	}

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
