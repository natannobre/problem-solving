class AssemblyLine
  def initialize(speed)
    @speed = speed
  end

  def production_rate_per_hour
    @speed * 221 * success_rate_multiplier
  end

  def working_items_per_minute
    (production_rate_per_hour / 60).to_i
  end

  private

  def success_rate_multiplier
    case @speed
    when 0
      0
    when 1..4
      1
    when 5..8
      0.9
    when 9
      0.8
    when 10
      0.77
    end
  end
end
