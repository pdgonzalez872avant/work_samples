require 'nokogiri'
require 'open-uri'

output = File.open("paddle_tournaments.txt", "w+")
output.write "date; name; location; contact;\n"

def wrangle(input)
  if input == nil
    return false
  else
    temp = ""
    input.each {|e| temp << "#{e.strip};" unless e.strip == ""}
    return "#{temp}|"
  end
end

doc = Nokogiri::HTML(open('http://www.platformtennis.org/Tournaments/APTA-Calendar.htm'))

data = doc.css("#content #right .calendar")

data.search("tr").each do |tr|
  temp = []
  final = []
  tr.search("td").each {|td| temp << td.text.split("\r\n")}

  date = wrangle(temp[1])
  final << date unless date == false

  name = wrangle(temp[3])
  final << name unless name == false

  location = wrangle(temp[4])
  final << location unless location == false

  contact = wrangle(temp[5])
  final << contact unless contact == false

  p final if final.length > 1
  output.puts "#{final.to_s}".sub("[", "").sub("]", "") if final.length > 1


end
