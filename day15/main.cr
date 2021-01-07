
Nums = [6, 19, 0, 5, 7, 13, 1]

def speak_sequence(finalTurn : Int32)
  lastSeen = Hash(Int32, Int32).new
  prev : Int32 = Nums[Nums.size - 1]

  (0...Nums.size).each do |i| 
    lastSeen[Nums[i]] = i 
  end

  (Nums.size...finalTurn).each do |i|
    curr : Int32
    if !lastSeen[prev]?
      curr = 0
    else
      curr = i-1-lastSeen[prev]
    end
    lastSeen[prev] = i - 1
    prev = curr
  end

  return prev
end

puts "Part 1\n#{speak_sequence(2020)}"
puts "\nPart 2\n#{speak_sequence(30_000_000)}"