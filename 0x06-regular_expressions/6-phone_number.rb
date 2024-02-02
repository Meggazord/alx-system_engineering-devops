#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

input_string = ARGV[0]

regex = /^\d{10}$/

match = input_string.match(regex)

if match
  puts "#{match[0]}"
else
  puts "No match"
end
