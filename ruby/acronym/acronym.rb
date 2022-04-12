class Acronym
  def self.abbreviate(string)
    abbreviation = ''
    string = string.gsub('-', ' ')
    arr = string.split
    arr.each do |word|
      abbreviation << word[0][0].upcase
    end

    abbreviation
  end
end
