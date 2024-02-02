#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

log_file_path = ARGV[0]

log_content = File.read(log_file_path)

regex = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/

matches = log_content.scan(regex)

matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
