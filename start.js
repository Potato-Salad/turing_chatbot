//start.js
function respond(response, bot_choice) {
    var spawn = require('child_process').spawn,
        py    = spawn('python', ['compute_input.py']),
        data = [response, bot_choice],
        dataString = '';

    py.stdout.on('data', function(data){
      dataString += data.toString();
    });
    py.stdout.on('end', function(){
      console.log('Response=',dataString);
    });
    console.log(JSON.stringify(data));
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
}

//Test Code
respond('hello',2)
