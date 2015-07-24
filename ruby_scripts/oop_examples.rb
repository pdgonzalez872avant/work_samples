# I've created this class to practice OOP. This is not complete, but definitely got me thinking on what to
# improve next. One could try to model how much a tennis player could spend for gear, maybe include traveling,
# eating, housing classes, and create a model where each class is called based on tournaments played.

# This is a decent start though. With the crux and a very personal item in a tennis players life, the racket.

class Racket

  attr_reader :tennis_string, :grip, :frame, :total_racket_cost

  def initialize(options = {})
    @tennis_string = options[:tennis_string]
    @grip = options[:grip]
    @frame = options[:frame]
    @total_racket_cost = tennis_string.cost + grip.cost + frame.cost
  end

  def restringing_with(new_string)
    if @tennis_string.break_string == true
      @tennis_string = new_string
      @total_racket_cost += new_string.cost
      return displays_cost
    else
      return "String still good"
    end

  end

  def displays_cost
    return "Your current total cost for this racket is #{@total_racket_cost}"
  end

  def display
    display = "This racket consists of the following items:\n"
    display += "#{@frame.display}#{@tennis_string.display}#{@grip.display}"
  end

end


class Frame

  attr_reader :manufacturer, :composition, :weight, :string_pattern, :display
  attr_accessor :color, :cost

  def initialize(options = {})
    @manufacturer = options[:manufacturer]
    @composition = options[:composition]
    @color = options[:color]
    @string_pattern = options[:string_pattern]
    @weight_grams =  options[:weight_grams]
    @cost = options[:cost]
  end

  def display
    @display = "---------------------------------------------------------\n" \
               "*** Frame *** \n" \
               "This is a #{@color} #{@manufacturer}, made of #{@composition}.\n" \
               "Weight is #{@weight_grams} with a stringing pattern of #{@string_pattern}.\n" \
               "Cost was $#{@cost}.\n"
    return @display
  end

end


class TennisString

  attr_reader :manufacturer, :composition, :gauge, :cost, :color
  attr_accessor :broken

  def initialize(options = {})
    @manufacturer = options[:manufacturer]
    @composition = options[:composition]
    @gauge = options[:gauge]
    @cost = options[:cost]
    @color = options[:color]
    @broken = false
  end

  def break_string
    @broken = true
  end

  def display
    @display = "---------------------------------------------------------\n" \
               "*** Tennis String *** \n" \
               "This is a #{@gauge} gauge #{@color} #{@manufacturer}, made of #{@composition}.\n" \
               "Cost was $#{@cost}.\n"
    return @display
  end

end


class Grip

  attr_accessor :color, :cost
  attr_reader :size

  def initialize(options = {})
    @size = options[:size]
    @color = options[:color]
    @cost = options[:cost]
  end

  def change_grip(color)
    @color = color
  end

  def display
    @display = "---------------------------------------------------------\n" \
               "*** Grip *** \n" \
               "This is a #{@size} #{@color} grip.\n" \
               "Cost was $#{@cost}.\n"
    return @display
  end

end


# Implementation:
frame = Frame.new({manufacturer: "Head",
                   composition: "Graphene",
                   color: "Yellow",
                   string_pattern: "16Mx19C",
                   weight_grams: 334.52,
                   cost: 150})

tennis_string = TennisString.new({manufacturer: "Luxilon",
                     composition: "Co-polymer (nylon) + Fluocarbon resin",
                     gauge: 16,
                     cost: 14.95,
                     color: "Beige"})

grip = Grip.new({size: "4 3/8",
                 color: "Black",
                 cost: 1})

racket = Racket.new({tennis_string: tennis_string,
                     grip: grip,
                     frame: frame})


cheaper_string = TennisString.new({manufacturer: "Kirschbaum",
                     composition: "Co-polymer monofilament",
                     gauge: 16,
                     cost: 8,
                     color: "Yellow"})


# # Driver test code

# puts frame.display
# puts tennis_string.display
# puts grip.display

# p racket.tennis_string.break_string
# p racket.restringing_with(cheaper_string)
# print racket.display
# p racket.grip.change_grip("pink")
# p racket.grip.color

