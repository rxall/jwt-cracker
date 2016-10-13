       ___  _    _ _____   _____                _               
      |_  || |  | |_   _| /  __ \              | |              
        | || |  | | | |   | /  \/_ __ __ _  ___| | _____ _ __   
        | || |/\| | | |   | |   | '__/ _` |/ __| |/ / _ \ '__|  
    /\__/ /\  /\  / | |   | \__/\ | | (_| | (__|   <  __/ |     
    \____/  \/  \/  \_/    \____/_|  \__,_|\___|_|\_\___|_|    

Shamelessly copied from:    
https://www.notsosecure.com/crafting-way-json-web-tokens/

Getting started:  
```
    pip install pyjwt
    pip install cryptography
```   
   
Ensure you set the algorithm to the corresponding token algorithm......  
Don't try and crack RS256 with HS256....  

The algorithm can be determined by base64 decoding the header:  
```
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9  
    {"alg":"HS256","typ":"JWT"}  
```
Payload in JWT format:   
```
[header].[payload].[signature]  
e.g. eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
```
