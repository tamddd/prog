typedef struct List {
  int data;
  struct List *next;
} List;

// struct ListをListと宣言できるようにしている
// typedef int foo;は、intをfooと宣言している
// 既存の型に別名をつけられるが、その対象がたまたま構造体なだけ。
