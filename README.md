## Docker command for starting immudb container

`docker run -d --net host -it --rm --name immudb codenotary/immudb:latest`
or
`docker run -d -p 5430:5432 -it --rm --name immudb codenotary/immudb:latest`

## CLI command to connect to immudb via psql

psql "host=localhost dbname=defaultdb user=immudb password=immudb sslmode=disable port=5430"
