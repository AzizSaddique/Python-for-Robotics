# n=int(input("Enter a number: "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# largest number
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# c = int(input("Enter a third number: "))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# sum of array
# arr = [1, 2, 3, 4, 5]
# total = sum(arr)
# print(total)

# reverse string
# s = input("Enter a string: ")
# reversed_s = s[::-1]
# print(reversed_s)

# factorial
# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

# palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:    print("Not Palindrome")







// #include <Arduino.h>
// #define RELAY_PIN 25

// void setup() {
//   Serial.begin(115200);
//   pinMode(RELAY_PIN, OUTPUT);

//   Serial.println("Relay FORCE ON (HIGH)");
//   digitalWrite(RELAY_PIN, HIGH);   // try HIGH
// }

// void loop() {
// }

// #include <Arduino.h>

// #define RELAY_PIN 25

// bool relayState = false;  // false = OFF, true = ON

// void setup() {
//   Serial.begin(115200);
//   pinMode(RELAY_PIN, OUTPUT);

//   // Most relay modules are ACTIVE LOW
//   digitalWrite(RELAY_PIN, HIGH); // OFF at start
//   relayState = false;
// }

// void loop() {

//   relayState = !relayState;  // toggle state

//   if (relayState) {
//     Serial.println("Relay ON");
//     digitalWrite(RELAY_PIN, LOW);   // ON (active LOW)
//   } else {
//     Serial.println("Relay OFF");
//     digitalWrite(RELAY_PIN, HIGH);  // OFF
//   }

//   delay(3000);
// }
