#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

input_string = ARGV[0]

regex = /hbt*n/

match = input_string.match(regex)

if match
  puts "#{match[0]}"
else
  puts "No match"
end
