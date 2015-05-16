# ruby scrips trying this out

#File.open()

# print Dir.pwd

f = File.new("text1.txt", "w")
f.write("Hi there")
f.close

=begin
File.open("my/file/path", "r") do |f|
  f.each_line do |line|
    puts line
  end
end
=end