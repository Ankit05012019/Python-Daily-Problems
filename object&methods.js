// ojects for for two pople with name mass, meging and a method to get their BMI


var Mark = {
             name: "Mark",
             height: 1.82,
             weight: 82,
             bmi: function(){ return this.weight/(this.height*this.height) }

};

var John = {
             name: "John",
             height: 1.82,
             weight: 82,
             bmi: function(){ return this.weight/(this.height*this.height)}
};

console.log(Mark.bmi());
console.log(John.bmi());

if( Mark.bmi() > John.bmi() ){
     console.log(Mark.name + " has a higher BMI which is " + Mark.bmi() );
} else if(Mark.bmi() < John.bmi()) {
    console.log(John.name + " has a higher BMI which is " + John.bmi() );
} else{
    console.log( John.name +"and"+ Mark.name +" both have equal BMI of " + John.bmi() )
}
