
var random_gradient_arr = [['#FF35EB', '#1E27FF'], ['#4DFFDF', '#FF1CBF'], ['#11C6FF', '#FFF500'], ['#FF1E1E', '#0060F1'], ['#54FF18', '#2E0CFF'], ['#FF1E6F', '#EFFF35'], ['#D7FF35', '#FF1E1E'], ['#88C606', '#FFD028', '#FF35EB']]
// Генерация рандомного числа.
function getRandomInt(max) {
	return Math.floor(Math.random() * Math.floor(max));
}
var random_gradient = getRandomInt(random_gradient_arr.length)
set_random_gradient_arr()

function set_random_gradient_arr(){
	let elems = ['logo']
	let logo = document.getElementById('logo')
	document.getElementById('logo').style.background = 'linear-gradient(90deg, '+random_gradient_arr[random_gradient][0]+', '+random_gradient_arr[random_gradient][1]+')'
	// Если кол-во цветов в массиве == 3, то есть градиент состоит из трех цветов, то:
	for (let elem of elems) {
		if(random_gradient_arr[random_gradient].length == 3){
			logo.style.background = 'linear-gradient(90deg, '+random_gradient_arr[random_gradient][0]+', '+random_gradient_arr[random_gradient][1]+', '+random_gradient_arr[random_gradient][2]+')'
			// $('#'+elem).css({
		 //   	 background: 'linear-gradient(90deg, '+random_gradient_arr[random_gradient][0]+', '+random_gradient_arr[random_gradient][1]+', '+random_gradient_arr[random_gradient][2]+')'
			// });
		}else{
			logo.style.background = 'linear-gradient(90deg, '+random_gradient_arr[random_gradient][0]+', '+random_gradient_arr[random_gradient][1]+')'
			// $('#'+elem).css({
		 //   		background: 'linear-gradient(90deg, '+random_gradient_arr[random_gradient][0]+', '+random_gradient_arr[random_gradient][1]+')'
			// });
		}
	}
}
