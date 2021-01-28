///calculate BMI JS

function Details(height,weight){

   this.height = height;
   this.weight = weight;

}

function Bmi(height,weight) {

      var bmi;
      bmi = weight/(height * height);
      return bmi;

}

var my = new Details("1.82","82");
var mark= new Details("1.96","96");


//console.log(my.height);
//console.log(my.weight);

var mybmi=Bmi(my.height,my.weight);
var markbmi=Bmi(mark.height,mark.weight);

if(mybmi > markbmi){

      console.log("my bmi grater than marks? " + Boolean(mybmi>markbmi))

} else {

         console.log("my bmi grater than marks? " + Boolean(mybmi>markbmi))
}
