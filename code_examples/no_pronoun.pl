#!/usr/bin/perl -w

use warnings;
use feature qw(say);

while ($line = <STDIN>) {
  $line =~ s/ab/ba/;
  say $line;
  say length $line;
}
