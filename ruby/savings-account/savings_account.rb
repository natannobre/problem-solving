module SavingsAccount
  def self.interest_rate(balance)
    case balance
    when ...0
      -3.213
    when 0..999.999
      0.5
    when 1000..4_999.999
      1.621
    else
      2.475
    end
  end

  def self.annual_balance_update(balance)
    balance * (1 + (interest_rate(balance) / 100).abs)
  end

  def self.years_before_desired_balance(current_balance, desired_balance)
    years = 1
    init = current_balance
    while annual_balance_update(init) <= desired_balance
      years += 1
      init = annual_balance_update(init).round(5)
    end
    years
  end
end
