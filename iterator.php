<?php


$arr = [
     '1' => "one",
     '2' => "two",
];

$itr = new ArrayObject($arr)->getIterator();

while ($itr->valid()) {
      echo $itr->key() . '=> ' . $itr->current() . "\n";
      $itr->next();
}