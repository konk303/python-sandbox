#!/usr/bin/env ruby

p 100.times.reduce([1, 1]) { |fib, i| i < 2 ? fib : fib << fib[i - 2] + fib[i - 1] }


def fib(nth)
  return 1 if nth < 2
  fib(nth - 2) + fib(nth - 1)
end

10.times { |i| puts "fib #{i}: #{fib(i)}" }
