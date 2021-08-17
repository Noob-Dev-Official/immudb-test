## Docker command for starting immudb container

`docker run -d --net host -it --rm --name immudb codenotary/immudb:latest` (for linux)
or
`docker run -d -p 5430:5432 -it --rm --name immudb codenotary/immudb:latest`
or
`docker run -p 3322:3322 -p 8080:8080 -it --rm --name immudb codenotary/immudb:latest` (for mac)

## Ports for immudb to open

**port 8080:** for web dashboard
**port 3322:** for immudb backend database server
**port 5432:** for immudb database access via psql

## CLI command to connect to immudb via psql

psql "host=localhost dbname=defaultdb user=immudb password=immudb sslmode=disable"
