#!/usr/bin/perl -w

use warnings;
use feature qw(say);

while (<STDIN>) {
  s/ab/ba/;
  say;
  say length;
}
