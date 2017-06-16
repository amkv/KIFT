var audio_context;

var recording = false;

var canvas = document.querySelector('.visualizer');

var audioCtx = new (window.AudioContext || webkitAudioContext)();
var canvasCtx = canvas.getContext("2d");



function startUserMedia(stream) {
  var input = audio_context.createMediaStreamSource(stream);
  console.log('Media stream created.');
  visualize(stream);
  recorder = new Recorder(input);
  console.log('Recorder initialised.');
}

function startRecording() {
  recorder.record();
  $("#record").css("background-color","#ef5350");
  // $("#record").addClass("waves-effect waves-light btn");
  $("#record").text("STOP");
}

function stopRecording() {
  $('#record').text("Waiting for response");
  $('#record').prop('disabled', true);

  recorder.stop();
  // $("#record").css("background-color","grey");
  // $("#record").text("Record");
  POSTAudioRequest();
  recorder.clear();
  // $("#record").text("Record");
}

function AddToConversation(json_object, from) {
  if (from == "user") {

    var $div = $("<div>", {"class": "elem_usr z-depth-2"});
    $div.prepend("You: " + json_object.text_input + "<p>");
    $("<audio></audio>").attr({
      'src':'/static/incoming/' + json_object.filePath_input,
      'controls':'controls'
    }).appendTo($div);

  }
  if (from == "machine") {

    var $div = $("<div>", {"class": "elem_machine z-depth-2"});
    $div.prepend("BLA: " + json_object.text_output + "<p>");
    $("<audio></audio>").attr({
      'src':'/static/outgoing/' + json_object.filePath_output,
      'controls':'controls',
      'autoplay':'autoplay'
    }).appendTo($div);
  }
  $("#conversation").prepend($div);
}

function POSTAudioRequest() {
  recorder.exportWAV(function(blob) {
   var reader = new FileReader();
   reader.onload = function() {
     $.ajax({
      url :  window.location.href + "submit",
      type: 'POST',
      data: blob,
      contentType: false,
      processData: false,
      success: function(data) {
        var json_object = JSON.parse(data);
        console.log(json_object);

        AddToConversation(json_object, "user");
        AddToConversation(json_object, "machine");

        var Hours = new Date().getHours();
        var Seconds = new Date().getMinutes();

        var $time = $("<p>TIME: " + Hours + ":" + Seconds + "<p>");
        $time.addClass("time");
        $("#conversation").prepend($time);
        $('#record').prop('disabled', false);
        $("#record").text("<i class=\"material-icons\">mic</i>");
        $("#record").text("Record");
        $("#record").css("background-color","#26a69a");
      },
      error: function() {
       console.log("Error");
       $('#record').prop('disabled', false);
       $("#record").text("Record");
       $("#record").css("background-color","#26a69a");
     }
   });
   }
   reader.readAsText(blob);
 });
}

window.onload = function init() {
  $("#record").on( "click", function(){
    if(recording)
    {
      console.log("Stop Recording");
      stopRecording();
      recording = false;
    }
    else
    {
      console.log("Recording");
      startRecording();
      recording = true;
    }
  });
  try {
    // webkit shim
    window.AudioContext = window.AudioContext || window.webkitAudioContext;
    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
    window.URL = window.URL || window.webkitURL;

    audio_context = new AudioContext;
    console.log('Audio context set up.');
    console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
  } catch (e) {
    alert('No web audio support in this browser!');
  }

  navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
    console.log('No live audio input: ' + e);
  });
};


// Nice to have, voice visualisation
function visualize(stream) {
  var source = audioCtx.createMediaStreamSource(stream);

  var analyser = audioCtx.createAnalyser();
  analyser.fftSize = 2048;
  var bufferLength = analyser.frequencyBinCount;
  var dataArray = new Uint8Array(bufferLength);

  source.connect(analyser);
  //analyser.connect(audioCtx.destination);

  WIDTH = canvas.width
  HEIGHT = canvas.height;

  draw()

  function draw() {

    requestAnimationFrame(draw);

    analyser.getByteTimeDomainData(dataArray);

    canvasCtx.fillStyle = 'rgb(255, 255, 255)';
    canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);

    canvasCtx.lineWidth = 2;
    canvasCtx.strokeStyle = 'rgb(108, 115, 114)';

    canvasCtx.beginPath();

    var sliceWidth = WIDTH * 1.0 / bufferLength;
    var x = 0;


    for(var i = 0; i < bufferLength; i++) {

      var v = dataArray[i] / 128.0;
      var y = v * HEIGHT/2;

      if(i === 0) {
        canvasCtx.moveTo(x, y);
      } else {
        canvasCtx.lineTo(x, y);
      }

      x += sliceWidth;
    }

    canvasCtx.lineTo(canvas.width, canvas.height/2);
    canvasCtx.stroke();

  }
}
