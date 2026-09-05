
class Temperature:

   @staticmethod
   def c_to_f(celsius):
       return f" {celsius}°C is equal to {(celsius * 9/5) + 32}°F"
   @staticmethod
   def f_to_c(fahrenheit):
       return f" {fahrenheit}°F is equal to {(fahrenheit - 32) * 5/9}°C"


t=Temperature()
a=t.c_to_f(56)
print(a)
b=t.f_to_c(132.8)
print(b)
