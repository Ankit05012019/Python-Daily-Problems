//tip calculator

var calculator = {

 bill: [124,48,268,180,42],
 tips: [],
 final:[],
 cal: function(){
      for (i=0;i<this.bill.length;i++){
          if (this.bill[i] < 50){ this.tips.push(this.bill[i]*.20);}
          else if (this.bill[i] > 50 && this.bill[i] < 200) {this.tips.push(this.bill[i]*.15);}
          else {this.tips.push(this.bill[i]*.10);}
        this.final.push((this.bill[i]+this.tips[i]))

      }


 }

}

console.log(calculator.bill)
calculator.cal();
console.log(calculator.tips)
console.log(calculator.final)
