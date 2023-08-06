/////////////////////////////////////////////////////////
// If cycleConfiguration is 1
// Thisprogram is for 1 Column PSA with a storage
// Valve 1 is for Column 1 Feed & Extract
// Valve 2 is for Column 1 Raffinate
// Valve 3 is for Storage Input
// Valve 4 is for STorage Output

/////////////////////////////////////////////////////////
// If cycleConfiguration is 2
// This program is for 2 Columns Basic 4-Step PSA
// Valve 1 is for Column 1 Feed & Extract
// Valve 2 is for Column 1 Raffinate
// Valve 3 is for Column 2 Feed & Extract
// Valve 4 is for Column 2 Raffinate

float pressurisation, adsorption, blowdown, purge;
int numberCycles;
int cycleConfiguration;

void setup() {
  pinMode( 7 , OUTPUT ); // Valve 1
  pinMode( 6 , OUTPUT ); // Valve 2
  pinMode( 5 , OUTPUT ); // Valve 3
  pinMode( 4 , OUTPUT ); // Valve 4
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming data string until a new line and is defined as "dataString"
    String dataString = Serial.readStringUntil('\n');

    // Split the data string into four float values and the number of cycles for the process
    int index = 0;
    // I use a string as an input from Python. Here, the dataString is converted into a
    // C - style language of a string which is essential in order to use the strtok() function.
    // The strtok() function is used convert the string into a token form. Based on the definition of token
    // (Token : sequence of characters having a collective meaning), the strtok() function confers a meaning
    // to the values in dataString. dataString is also separated into multiple values using the delimiter ",".
    // The char* ptr section creates a pointer variable named ptr that will be used to 
    // store the address of the token returned by strtok().
    char* ptr = strtok((char*)dataString.c_str(), ",");
    while (ptr != NULL && index < 6) {
      if (index == 0) pressurisation = atof(ptr);
      else if (index == 1) adsorption = atof(ptr);
      else if (index == 2) blowdown = atof(ptr);
      else if (index == 3) purge = atof(ptr);
      else if (index == 5) numberCycles = atoi(ptr);
      else if (index == 4) cycleConfiguration = atoi(ptr);

      ptr = strtok(NULL, ",");
      index++;
    }

    // The while (ptr != NULL && index < 5) section initiates a loop that continues as long as 
    // ptr is not NULL (i.e., there are more tokens to process) and index is less than 5. 
    // The purpose of this loop is to process up to 5 tokens (comma-separated values) from the original string.
    // The if and else if statements converts the token into floating values and assign them to their respective variable name.

    // Run the process cycle for the specified number of loops/cycles

    if (cycleConfiguration == 1) {

    // Run the process cycle for the specified number of loops/cycles
    for (int loop = 0; loop < numberCycles; loop++) {
      
      // This is for pressurisation process
      // The delay(pressurisation) determines how long the pressurisation process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, LOW); // Valve 2 position
      digitalWrite(5, LOW); // Valve 3 position
      digitalWrite(4, LOW); // Valve 4 position
      String p1 = ";";
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Close" + p1 + "Valve 3 Close" + p1 + "Valve 4 Close"); // Print Valves positions
      delay(pressurisation); // Pressurisation time
      

      // This is for adsorption process
      // The delay(adsorption) determines how long the adsorption process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, HIGH); // Valve 2 position
      digitalWrite(5, LOW); // Valve 3 position
      digitalWrite(4, HIGH); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Close" + p1 + "Valve 4 Open"); // Print Valves positions
      delay(adsorption); // Adsorption time     

      // This is for blowdown process
      // The delay(blowdown) determines how long the blowdown process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, LOW); // Valve 2 position
      digitalWrite(5, LOW); // Valve 3 position
      digitalWrite(4, LOW); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Close" + p1 + "Valve 3 Close" + p1 + "Valve 4 Close"); // Print Valves positions
      delay(blowdown); // Blowdown time
      
      // This is for purge process
      // The delay(purge) determines how long the purge process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, HIGH); // Valve 2 position
      digitalWrite(5, LOW); // Valve 3 position
      digitalWrite(4, HIGH); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Close" + p1 + "Valve 4 Open"); // Print Valves positions
      delay(purge); // Purge time

    }

      // When the process is completed i.e. the number of cycles has been satisfied, all valves open to
      // signify that the process is ceased.
      // The connection from Python to Arduino is closed
      digitalWrite( 7, HIGH);
      digitalWrite( 6, HIGH);
      digitalWrite( 5, HIGH);
      digitalWrite( 4, HIGH);
      String p1 = ";";
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Open" + p1 + "Valve 4 Open"); // Print Valves positions
  }

  if (cycleConfiguration == 2) {

    for (int loop = 0; loop < numberCycles; loop++) {
      
      // This is for pressurisation process for Column 1 and blowdown for Column 2
      // The delay(pressurisation) determines how long the pressurisation process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, LOW); // Valve 2 position
      digitalWrite(5, HIGH); // Valve 3 position
      digitalWrite(4, LOW); // Valve 4 position
      String p1 = ";";
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Close" + p1 + "Valve 3 Open" + p1 + "Valve 4 Close"); // Print Valves positions
      delay(pressurisation); // Pressurisation time
      

      // This is for adsorption process for Column 1 and purge for Column 2
      // The delay(adsorption) determines how long the adsorption process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, HIGH); // Valve 2 position
      digitalWrite(5, HIGH); // Valve 3 position
      digitalWrite(4, HIGH); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Open" + p1 + "Valve 4 Open"); // Print Valves positions
      delay(adsorption); // Adsorption time     

      // This is for blowdown process for Column 1 and pressurisation for Column 2
      // The delay(blowdown) determines how long the blowdown process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, LOW); // Valve 2 position
      digitalWrite(5, HIGH); // Valve 3 position
      digitalWrite(4, LOW); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Close" + p1 + "Valve 3 Open" + p1 + "Valve 4 Close"); // Print Valves positions
      delay(blowdown); // Blowdown time
      
      // This is for purge process for Column 1 and adosrption for Column 2
      // The delay(purge) determines how long the purge process is
      digitalWrite(7, HIGH); // Valve 1 position
      digitalWrite(6, HIGH); // Valve 2 position
      digitalWrite(5, HIGH); // Valve 3 position
      digitalWrite(4, HIGH); // Valve 4 position
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Open" + p1 + "Valve 4 Open"); // Print Valves positions
      delay(purge); // Purge time

    }

      // When the process is completed i.e. the number of cycles has been satisfied, all valves open to
      // signify that the process is ceased.
      // The connection from Python to Arduino is closed
      digitalWrite( 7, HIGH);
      digitalWrite( 6, HIGH);
      digitalWrite( 5, HIGH);
      digitalWrite( 4, HIGH);
      String p1 = ";";
      Serial.println( "Valve 1 Open" + p1 + "Valve 2 Open" + p1 + "Valve 3 Open" + p1 + "Valve 4 Open"); // Print Valves positions
  }

  }
}