/**ProyectoF 2016 **    https://youtu.be/V7R1cG3y84c
informacion de las librerias  https://github.com/TMRh20/TMRpcm
                              http://playground.arduino.cc/Main/CapacitiveSensor
*/
//líbrerias necesarias 
#include <CapacitiveSensor.h>


CapacitiveSensor   cs_14_2 = CapacitiveSensor(90,19); // define pines en arduino uno el 14 es A0.
CapacitiveSensor   cs_14_3 = CapacitiveSensor(90,21);
CapacitiveSensor   cs_14_4 = CapacitiveSensor(90,35);
CapacitiveSensor   cs_14_5 = CapacitiveSensor(90,37);
CapacitiveSensor   cs_14_6 = CapacitiveSensor(90,39);
CapacitiveSensor   cs_14_7 = CapacitiveSensor(90,41);
CapacitiveSensor   cs_14_8 = CapacitiveSensor(90,51);

int sense = 400;  // define sencibilidad a menor numero mas sencible
int tiempo = 100; // define tiempo maximo de reproduccion


void setup(){
  Serial.begin(9600);
}

void loop(){  
 long valor1 =  cs_14_2.capacitiveSensor(20);
 if (valor1 > 0){
  Serial.println(valor1);
  Serial.println("valor1");
 }
 long valor2 =  cs_14_7.capacitiveSensor(20);
 if (valor2 > 0){
  Serial.println(valor2);
  Serial.println("valor2");
 }
 long valor3 =  cs_14_8.capacitiveSensor(20);
 if (valor3 > 0){
  Serial.println(valor3);
  Serial.println("valor3");
 }
 
}
