// JS coding exercise

var bills = new Array();
var tips = [];

bills.push(124);
bills.push(48);
bills.push(268);

//console.log(bills)

var i = bills.length
var j = 0

while (j < i ){

   if ( bills[j] < 50 ){
   tips[j] = bills[j] * 0.20;
 }  else if ( bills[j] > 50 && bills[j] < 200){
    tips[j] = bills[j] * 0.15;
  } else{
    tips[j] = bills[j] * 0.10;
  }

  j += 1

}
console.log("bills paid are " + bills)

console.log( "tips calculated are " + tips )
