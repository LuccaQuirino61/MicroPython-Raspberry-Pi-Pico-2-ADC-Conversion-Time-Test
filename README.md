# Testing the conversion time of the Raspberry Pi Pico 2 ADC using MicroPython, to be used in a control system with PWM at 50kHz

## Project Description
This project aims to test the ADC conversion time of a Raspberry Pi Pico 2 programmed using MicroPython, to be applied in a control system with a PWM at 50kHz frequency using 2 ADC.

## Project Structure
- **MicroPython Code:** Programming structure to evaluate the period it takes for the ADC to convert.
- **Analysis Report:** Results obtained experimentally by running the code.

## Requirements
- Raspberry Pi Pico 2
- MicroPython firmware installed
- Thonny or another MicroPython-compatible IDE
- Libraries to install:
  - machine
  - utime

## Setup Instructions
1. Flash the MicroPython firmware onto the Raspberry Pi Pico 2.
2. Upload the provided MicroPython script to the board.
3. Run the script and observe the ADC conversion time.
4. Analyze the results and compare them with the system's requirements.

## Expected Outcome
As we are working with a PWM frequency of 50kHz, the period of one cycle of our system is 20us. Therefore, we need the two ADC conversion time to be less than 20us.

## Results
The average conversion time of the two ADCs was **16.54us** after 100 PWM cycle periods.
Therefore, for a period of 20us of PWM, we achieved, with two ADCs, a satisfactory response time for a real-time control system.

## Author
Lucca Pereira Parenti Quirino, Electrical Engineering Student - INEP - UFSC

