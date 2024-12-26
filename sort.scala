def rankedWords(wordScore : String => Int, words : List[String]) : List[String] = {
  def score(word : String) : Int = {
    word.replace("a", "").length
  }
  words.sortBy(score)
}