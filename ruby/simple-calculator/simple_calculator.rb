class SimpleCalculator
  class UnsupportedOperation < StandardError
  end

  ALLOWED_OPERATIONS = ['+', '/', '*'].freeze

  def self.calculate(first_operand, second_operand, operation)
    raise UnsupportedOperation unless ALLOWED_OPERATIONS.include?(operation)
    raise ArgumentError unless (first_operand.kind_of?(Integer) && second_operand.kind_of?(Integer))

    if operation == '+'
      add(first_operand, second_operand)
    elsif operation == '*'
      multiply(first_operand, second_operand)
    elsif operation == '/'
      divide(first_operand, second_operand)
    end
  end

  def self.divide(first_operand, second_operand)
    return "Division by zero is not allowed." if second_operand == 0

    "#{first_operand} / #{second_operand} = #{first_operand / second_operand}"
  end

  def self.add(first_operand, second_operand)
    "#{first_operand} + #{second_operand} = #{first_operand + second_operand}"
  end

  def self.multiply(first_operand, second_operand)
    "#{first_operand} * #{second_operand} = #{first_operand * second_operand}"
  end
end