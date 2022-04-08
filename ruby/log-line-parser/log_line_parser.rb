class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    @line.split(': ', 2)[1].strip
  end

  def log_level
    @line.split(': ', 2)[0].delete('[]').downcase
  end

  def reformat
    m = message
    l = log_level

    "#{m} (#{l})"
  end
end
