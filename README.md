## Docker command for starting immudb container

`docker run -d --net host -it --rm --name immudb codenotary/immudb:latest` (for linux)
or
`docker run -d -p 5430:5432 -it --rm --name immudb codenotary/immudb:latest`
or
`docker run -p 3322:3322 -it --rm --name immudb codenotary/immudb:latest` (for mac)

## CLI command to connect to immudb via psql

psql "host=localhost dbname=defaultdb user=immudb password=immudb sslmode=disable"
