const array = [0,50,75,-1,100,-20,15];

array.sort(function(a,b){return a-b});

console.log("2nd Minimum is",array[1]);
console.log("2nd Maximum is",array[array.length-2]);
