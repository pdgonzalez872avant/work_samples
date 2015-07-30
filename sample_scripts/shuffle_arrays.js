// Create function that takes array and returns a shuffled array.
function shuffleArray(input_array){

  // Returns a random number given an interval
  // stackoverflow.com/questions/4959975/generate-random-value-between-two-numbers-in-javascript
  function randomIntFromInterval(min,max){
      return Math.floor(Math.random() * (max - min + 1) + min);
  }

  // Creates temp array
  var shuffled_array = []
  var random_number_array = []

  // Will create an array with random non-repeating numbers
  for (var index = 0; index < input_array.length; index++){

    // creates boolen trigger
    var stop_now = false

    // Brute force to create a random array
    while (stop_now == false){

      // Creates random number
      var random_between = randomIntFromInterval(0, input_array.length - 1)

      // Sanity check
      // console.log("This is the random number: " + random_between)

      // conditional to test if number is already in array with indexOf
      // indexOf return -1 when there is no match inside the array, therefore the element is unique
      if (random_number_array.indexOf(random_between) == "-1"){

        // if it is not in the array, add to the array
        random_number_array.push(random_between)

        // Since we added the item to the array, stop while loop
        stop_now = true

      } else{

        continue; // Continues iteration if no match
      }
    }
  }

  // adds to shuffled array based on the random number index
  for (var index = 0; index < input_array.length; index++){

    // the random_number_index contains the random indexes. We slice the array and therefore have a shuffled index
    var shuffled_index = random_number_array[index]

    // We use the shuffled index to push to the shuffled_array.
    shuffled_array.push(input_array[shuffled_index])

    // // Sanity check
    // console.log("input_array[not_shuffled]= " + input_array[index] + " -- input_array[shuffled] = " + input_array[shuffled_index])
  }

  // // Displays the random number array
  // console.log(random_number_array)

  return shuffled_array
}

a = ["Paulo", "Nick", "Paul", "Lily"]

console.log(shuffleArray(a))