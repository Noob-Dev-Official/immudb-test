## Docker command for starting immudb container

`docker run -d --net host -it --rm --name immudb codenotary/immudb:latest`
or
`docker run -d -p 5430:5430 -it --rm --name immudb codenotary/immudb:latest`
