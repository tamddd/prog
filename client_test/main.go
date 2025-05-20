package main

import "net"

func main() {
	_, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		panic(err)
	}
}
