var i = 0;
console.log("Entering the loop!<br /> ");
        outerloop:     // This is the label name

         while (i<3) {
            console.log("Outerloop: " + i + "<br />");
            i += 1;
            for (var j = 0; j < 5; j++) {
               if (j == 3) {
                  continue outerloop;
               }
               console.log("Innerloop: " + j + "<br />");
            }
    
         }

console.log("Exiting the loop!<br /> ");
