class Exp {}

sealed abstract class Exp
case class Add(lhs: Exp, rhs:Exp) extends Exp
case class Sub(lhs: Exp, rhs:Exp) extends Exp
case class Mul(lhs: Exp, rhs:Exp) extends Exp
case class Div(lhs: Exp, rhs:Exp) extends Exp
case class Lit(value: Int) extends Exp

val emam = Add(Lit(1), Lit(2))

def eval(exp: Exp): Int = exp match {
    case Add(lhs, rhs) => eval(lhs) + eval(rhs)
    case Sub(lhs, rhs) => eval(lhs) - eval(rhs)
    case Mul(lhs, rhs) => eval(lhs) * eval(rhs)
    case Div(lhs, rhs) => eval(lhs) / eval(rhs)
    case Lit(value) => value
}
