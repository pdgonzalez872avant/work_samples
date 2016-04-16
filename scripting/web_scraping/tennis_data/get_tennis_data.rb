require 'nokogiri'
require 'open-uri'

# challenger/futures
doc = Nokogiri::HTML(open("http://www.atpworldtour.com/en/atp-challenger-tour"))
last_week = doc.css(".event-listing #futures #itf-lastWeek")


# get_data_atp_tournaments
# doc = Nokogiri::HTML(open('http://www.atpworldtour.com/en/tournaments')


# data = doc.css("#content #right .calendar")
#
# data.search("tr").each do |tr|
#   temp = []
#   final = []
#   tr.search("td").each {|td| temp << td.text.split("\r\n")}
#
#   date = wrangle(temp[1])
#   final << date unless date == false
#
#   name = wrangle(temp[3])
#   final << name unless name == false
#
#   location = wrangle(temp[4])
#   final << location unless location == false
#
#   contact = wrangle(temp[5])
#   final << contact unless contact == false
#
#   p final if final.length > 1
#   output.puts "#{final.to_s}".sub("[", "").sub("]", "") if final.length > 1
# end
