object Option {
  def main(args: Array[String]) = {

    val stock = Map("Ice Tea" -> 9,
                    "Kong Strong" -> None)

    println("Ice Tea : " + stock.get("Ice Tea"))
    println("Ice Tea : " + stock.get("Ice Tea").get)

    println()

    println("Kong Strong : " + stock.get("Kong Strong"))
    println("Kong Strong : " + stock.get("Kong Strong").get)

    println()

    println("Fanta Cringe : " + stock.get("Fanta Cringe"))

    println()

    stock.get("Kong Strong") match {
        case Some(i) => println("Match: " + i)
        case None => println("Kong Strong does not exists")
    }

    println()

    stock.get("Fanta Cringe") match {
        case Some(i) => println("Match: " + i)
        case None => println("Fanta Cringe does not exists")
    }
  }
}
