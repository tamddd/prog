package main

import (
	"fmt"
	"net"
)

func main() {
	listner, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		fmt.Println(err)
		return
	}

	con, err := listner.Accept()
	if err != nil {
		fmt.Println(err)
		return
	}

	hanlder(con)
}

func hanlder(con net.Conn) {
	buf := make([]byte, 2<<10)
	n, err := con.Read(buf)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(buf[:n]))
}
