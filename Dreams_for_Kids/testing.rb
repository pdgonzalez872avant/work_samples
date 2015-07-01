class Prices
  attr_accessor :var_prices

  def to_s
    "This is the Prices class #{@var_prices}"
  end

  def var_prices
    @var_prices = [1,2,3,4]
  end
end

module Girls
  attr_accessor :var_girls
  @var_girls = ["hot", "amazing", "great"]
end

