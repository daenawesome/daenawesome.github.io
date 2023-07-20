
let currentDateAndTime = Date()

console.log("It is now "+currentDateAndTime)


let theTotal = total("the", "brown", "fox", "jumps", "over", "the", "lazy", "doug", "then", "what?")

console.log("The total is "+theTotal)


function total(...theNumbers){
	let sum = 0
	for(let aNumber in theNumbers){
		sum += aNumber*1//Want to know why aNumber is multiplied by 1? Remove it and find out. :)
	}
	return sum
}
