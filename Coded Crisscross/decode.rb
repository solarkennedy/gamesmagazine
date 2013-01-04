#!/usr/bin/env ruby
counter = 0
lines = []
file = File.new("coded.txt", "r")
while (line = file.gets)
    counter = counter + 1
    lines[counter] = line.split.map{|x|(x.to_i+64).chr}
    puts "#{lines[counter].inject(:+)}"
end
file.close

puts ""
puts "Now go to http://www.blisstonia.com/software/WebDecrypto/index.php and paste it in with Patristocrat mode"
puts "Or get http://www.blisstonia.com/software/Decrypto/#download to solve the cryptoquote for you"
