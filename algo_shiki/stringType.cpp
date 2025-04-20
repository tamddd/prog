#include <bits/stdc++.h>
#include <string>
using namespace std;

string typeDetermination(char c){
  if ('a' <= c && c <= 'z') {
	return "lowercase";
  } else if ('A' <= c && c <= 'Z'){
	return "uppercase";
  } else if ('0' <= c && c <= '9'){
	return "digit";
  } else {
    return string(1, c);
  }
}

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  for (char c : s) {
	cout << typeDetermination(c) << endl;
  }
}
